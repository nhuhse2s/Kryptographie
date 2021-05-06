####
# This program aims to crack an One-Time-Pad
####

import numpy as np
import pip._vendor.chardet as ch

def Decrypt(ciphertext, key):
    assert(len(ciphertext) < len(key))

    cipherLength = len(ciphertext)
    keyLength = len(key)
    counterFirstXOR = 0
    de_cipher = []
    tempList = []

    for shift in range(0, keyLength):

        strList = ""
        currentXOR = None  
        firstXOR = ciphertext[0] ^ key[counterFirstXOR]

        if ((firstXOR < 32) or (firstXOR > 128)): 
            counterFirstXOR += 1
            continue
        
        for n in range(0,cipherLength):
            if(n+counterFirstXOR < keyLength):
                currentXOR = ciphertext[n]^key[n+counterFirstXOR]
            if((currentXOR < 32) or (currentXOR > 128)):
                break
            de_cipher.append(currentXOR)
        
        for x in de_cipher:
            tempList.append(chr(x))
        strList = "".join(tempList)
        
        if(len(strList) > 200):
            print("......cracking......\n")
            print("KeyPosition: ", counterFirstXOR)
            print("Plaintext found: ", strList, "\n")


        counterFirstXOR += 1
        tempList.clear()
        de_cipher.clear()
        strList = ""
        
    return  

def Main():
    c = open("data/chiffrat.bin", "rb").read()
    k = open("data/random.dat", "rb").read()

    print(Decrypt(c, k))

if __name__ == "__main__":
    Main()