##
import re 

##
chiffre = ""
encryptedChiffre = ""
letterFrequency = {}
germanLetterFrequency = [0.174, 0.0978, 0.0755, 0.0727, 0.07, 0.0651, 0.0615,
                            0.0508, 0.0476, 0.0435, 0.0344, 0.0306, 0.0301, 0.0253,
                            0.0251, 0.0189, 0.0189, 0.0166, 0.0121, 0.0113, 0.0079,
                            0.0067, 0.0031, 0.0027, 0.0004, 0.0003, 0.0002]
germanLetterFrequencyX = ["E", "N", "I", "S", "R", "A", "T", "D", "H", "U", "L", "C", "G", "M",
                             "O", "B", "W", "F", "K", "Z", "P", "V", "J", "Y", "X", "Q"]

## Durch Ausprobieren herausfinden
fixedLetterFrequencyX = ["V", "Q", "O", "U", "N", "K", "M", "B", "C", "F", "W", "G", "E",
                            "T", "D", "X", "H", "I", "A", "J", "P", "R", "Z", "L", "Y", "S"]
germanDict = dict(zip(germanLetterFrequencyX, germanLetterFrequency))

def OpenFile(path: ""):
    return open(path).read()  

def CalculateFrequency(chifText: {}) -> {}:
    letters = [chr(i) for i in range(65,91)]
    for i in letters:
        letterFrequency[i] = chifText.count(i)   
    return letterFrequency

def Encryption(chifText, alphabet):
    freq = CalculateFrequency(chifText)
    freqSorted = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    tempDict = dict(zip(fixedLetterFrequencyX, alphabet.keys()))
    
    encryptedText = ""

    for char in chifText:
        if re.match("[^A-Z]+", char):
            encryptedText += char
        else: 
            encryptedText += str(tempDict.get(char))

    return encryptedText
    

def Main():
    chiffre = OpenFile("chiffrat.txt")
    encryptedChiffre = Encryption(chiffre, germanDict)
    print(encryptedChiffre)
    
if __name__ == "__main__":
    Main()