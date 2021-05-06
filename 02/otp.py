import numpy as np
import base64

def Main():
    cipher = open("data/chiffratbin.sec", "rb").read()
    key = open("data/random.dat", "rb").read()
    #keyList = key.tolist()
    #print(keyList)
    #print(key)
    print("cipher", type(cipher))
    print("key", type(key))
    print(cipher[0])
    #print(cipher)
    #print(keyList[0])
    #l = []
    a = cipher[0]^key[0]
    b = cipher[1]^key[1]
    c = cipher[2]^key[2]
    d = cipher[3]^key[3]
    #l.append(a)
    print("XOR",a ,chr(a), chr(b), chr(c), chr(d))
    
    #for k in key.tolist():
    #    print(type(k))

if __name__ == "__main__":
    Main()