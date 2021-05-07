####
# This program aims to crack One-Time-Pad messages, which where encrypted with the same keys
####

def Decrypt(message01, message02, message03):
    assert(len(message01) == len(message02) and (len(message02) == len(message03)))

    messageLength = len(message01)

    m1_int = []
    m2_int = []
    m3_int = []
    m1_xor_m2 = []
    m1_xor_m3 = []
    m2_xor_m3 = []

    guessedWord = "China" # Corona, Deutschland, Bericht, Wetter, Sonne, RKI, Russland, USA, Biden
    guessedWord_int = []
    
    for n in range(0, messageLength):
        m1_int.append(ord(message01[n]))
        m2_int.append(ord(message02[n]))
        m3_int.append(ord(message03[n]))

    for n in range(0, messageLength):
        m1_xor_m2.append(m1_int[n]^m2_int[n])
        m1_xor_m3.append(m1_int[n]^m3_int[n])
        m2_xor_m3.append(m2_int[n]^m3_int[n])

    for c in guessedWord:
        guessedWord_int.append(ord(c))

    counterFirstXOR = 0
    firstXOR = 0
    de_cipher = []
    tempList = []

    for shift in range(0, messageLength):

        strList = ""
        currentXOR = None

        if(counterFirstXOR < len(guessedWord_int)):  
            firstXOR = m1_xor_m2[0] ^ guessedWord_int[counterFirstXOR]

        if ((firstXOR < 32) or (firstXOR > 128)): 
            counterFirstXOR += 1
            continue
        
        for n in range(0, messageLength):
            if(n+counterFirstXOR < len(guessedWord_int)):
                currentXOR = m1_xor_m2[n]^guessedWord_int[n+counterFirstXOR]
            else: 
                break
            #if((currentXOR < 32) or (currentXOR > 128)):
            #    break
            de_cipher.append(currentXOR)
        
        for x in de_cipher:
            tempList.append(chr(x))
        strList = "".join(tempList)

        print("Found: ", strList)

        counterFirstXOR += 1
        tempList.clear()
        de_cipher.clear()
        strList = ""

    print("m1_xor_m2: ", m1_xor_m2)
    print("m1_xor_m3: ", m1_xor_m3)
    print("m2_xor_m3: ", m2_xor_m3)
    print("guessedWord: ", guessedWord)
    print("int_word: ", guessedWord_int)
    print()
    

    return

def Main():
    f = open("data/chiffrat2.txt").read()
    ciphertext = f.split()
    m01 = ciphertext[0]
    m02 = ciphertext[1]
    m03 = ciphertext[2]
    Decrypt(m01, m02, m03)

if __name__ == "__main__":
    Main()