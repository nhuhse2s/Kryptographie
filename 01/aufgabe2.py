import re

letterFrequency = {}
germanLetterFrequency = [0.174, 0.0978, 0.0755, 0.0727, 0.07, 0.0651, 0.0615,
                            0.0508, 0.0476, 0.0435, 0.0344, 0.0306, 0.0301, 0.0253,
                            0.0251, 0.0189, 0.0189, 0.0166, 0.0121, 0.0113, 0.0079,
                            0.0067, 0.0031, 0.0027, 0.0004, 0.0003, 0.0002]

germanLetterFrequencyX = ["E", "N", "I", "S", "R", "A", "T", "D", "H", "U", "L", "C", "G", "M",
                             "O", "B", "W", "F", "K", "Z", "P", "V", "J", "Y", "X", "Q"]

germanDict = dict(zip(germanLetterFrequencyX, germanLetterFrequency))

def OpenFile(path: ""):
    return open(path).read()  

def CalculateFrequency(chifText: {}) -> {}:
    letters = [chr(i) for i in range(65,91)]
    for i in letters:
        letterFrequency[i] = chifText.count(i)           
    return letterFrequency

def Koinzidenz(text, length):
    # print(f'Koinzidenz berechnen für {x} mit Schlüssellänge {l}')
    c = []
    for i in range(length):
        c.append(text[i::length])
    #print(c)
    koninz = 0
    # print(f'Chunk splitting: {c}')
    # print('-------------------')
    for chunk in c:
        chunk = list(chunk)
        # print(chunk)
        dic = {i: chunk.count(i) for i in chunk}
        duplikate = 0
        for v in dic.values():
            if v > 1:
                duplikate += v * (v - 1)
        k = duplikate / (len(chunk) * (len(chunk) - 1))
        koninz += k
        # print(f'Berechne: {duplikate} / ({len(chunk)} * {len(chunk) - 1})')
        # print(f'Teil-Koinzidenz: {k:.3f}')
        # print('-------------------')
    koninz /= length
    return koninz

def ReconstructKeyLength(x, min, max):
    print('Rekonstruiere Key-Length mittels Koinzidenz:')
    print()
    d = {}
    for i in range(min, max + 1):
        k = Koinzidenz(x, i)
        d[i] = k
        print(f'Koinzidenz für Schlüssellänge {i}: {k}')
        # print('---------------------')
    print()
    # print(f'Berechnete Schlüssel:')
    # print_dict(d)
    v = list(d.values())
    k = list(d.keys())

    curr = 0
    for i in v:
        if i > curr:
            curr = i
    mostprob = k[v.index(curr)]

    print(f'Wahrscheinlichste Schlüssellänge: {mostprob}')

def SpeziellerKoinzidenz(text, length):
    chunks = []
    for i in range(length):
        chunks.append(text[i::length])

    koninz = 0
    for chunk in chunks:
        chunk = list(chunk)
        dic = {i: chunk.count(i) for i in chunk}
        duplikate = 0
        sum = 0
        print("chunk :" + str(dic))
        for key, value in dic.items():
            if re.match("[A-Z]+", str(key)):
                sum += value*germanDict[key]
                #print(sum)
                #print("key " + key)


def Main():
    chiffre = OpenFile("chiffrat2.txt")
    #print(CalculateFrequency(chiffre))   
    #print(Koinzidenz(chiffre, 10))
    #ReconstructKeyLength(chiffre, 1, 10)
    SpeziellerKoinzidenz(chiffre, 10)

if __name__ == "__main__":
    Main()