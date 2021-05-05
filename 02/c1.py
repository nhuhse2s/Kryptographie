####
# This program aims to crack an One-Time-Pad
####

import numpy as np

def Decrypt(ciphertext, key):
    counter = 0
    l = []
    keyList = []
    for i in key.tolist():
        keyList.append(i.to_bytes)

    print(keyList)
    #print(type(keyList1))
    #keyBytes = [abs(i) for i in key]
    #print(keyBytes)
    for i in ciphertext:
        l.append(i ^ (key[counter]))    ## XOR operation
        counter += 1
    #result = [abs(i) for i in l]
    return l

def Main():
    c = open("data/chiffratbin.sec", "rb").read()
    k = np.fromfile("data/random.dat", dtype="byte")
    #print(type(c))
    #print(k)
    #print(Decrypt(c, k))
    Decrypt(c, k)

if __name__ == "__main__":
    Main()