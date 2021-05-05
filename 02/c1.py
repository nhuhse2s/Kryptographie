####
# This program aims to crack an One-Time-Pad
####

import numpy as np

def Decrypt(ciphertext, key):
    counter = 0
    l = []
    keyBytes = []
    
    for i in key.tolist():
        keyBytes.append(i.to_bytes(1, "little", signed=True))


    a = (keyBytes[0])
    b = (ciphertext[0].to_bytes(1, byteorder="little"))
    print((keyBytes[0]))
    print("test", ciphertext[0])
    print((ciphertext[0].to_bytes(1, byteorder="little")))

    bytesCipherText = []
    for number in ciphertext:
        bytesCipherText.append(number.to_bytes(1, byteorder="little"))

    print(bytesCipherText)
    #result = bytearray(bytesCipherText)
    #for counter, key in enumerate(keyBytes):
     #   bytesCipherText[counter] ^= key

    # for i in ciphertext:
    #     l.append(i.to_bytes(1, "little") ^ keyList[counter])    ## XOR operation
    #     counter += 1

    return 

def Main():
    c = open("data/chiffratbin.sec", "rb").read()
    k = np.fromfile("data/random.dat", dtype="byte")
    #print(type(c))
    #print(k)
    #print(Decrypt(c, k))
    Decrypt(c, k)

if __name__ == "__main__":
    Main()