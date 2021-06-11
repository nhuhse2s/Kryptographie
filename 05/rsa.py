###############################
### RSA Key Generation, Encryption & Decryption
###############################
from Crypto.Util import number
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from timeit import default_timer as timer
import Crypto.Math
import random
import math as m

def RSA_a():  
    prime_length = 1500
    for x in range(0,10):
        start = timer()
        prime_number = number.getPrime(prime_length)
        end = timer()
        print("x: ", x, "| time: ", end - start, " Sekunden")

def RSA_b():
    prime_length = 3000
    ggt          = 0
    prime_p      = number.getPrime(prime_length)    
    prime_q      = number.getPrime(prime_length)
    n            = prime_p*prime_q                  
    phi_n        = (prime_p-1)*(prime_q-1)          
    #e            = (2**16)+1
    while True:
      e = random.randrange(2 ** (prime_length - 1), 2 ** (prime_length))
      if m.gcd(e, phi_n) == 1 & (e < phi_n):
         break
                                     
    d = pow(e, -1, phi_n)
    #d1 = Crypto.Math.findModInverse(e, phi_n)
    #print("d: ",d)
    #print("d1: ",d1)                
        
    # prime_p      = 5    
    # prime_q      = 11    
    # n            = 55                 
    # phi_n        = 40         
    # e            = 17                      
    # d            = modinv(e, phi_n)                 
    return prime_p, prime_q, phi_n, n, e, d

def RSA_encrypt(x, e, n):
    return (x**e)%n

def RSA_decrypt(x, d, n):
    return (x**d)%n

def ModInv(e, phi):
    d_old = 0; r_old = phi
    d_new = 1; r_new = e
    while r_new > 0:
        a = r_old // r_new
        (d_old, d_new) = (d_new, d_old - a * d_new)
        (r_old, r_new) = (r_new, r_old - a * r_new)
    return d_old % phi if r_old == 1 else None

def GGT(a, b):
    while b!=0:
        c=a%b
        a=b
        b=c
    return a

if __name__ == "__main__":

    #RSA_a()

    p, q, phi_n, n, e, d = RSA_b()
    # print("p: ", p)
    # print("q: ", q)
    # print("phi: ", phi_n)
    # print("n: ", n)
    # print("e: ", e)
    # print("d: ", d)
    
    message = b'helloworld'
    print("----building keys------")
    public_key = RSA.construct((n, e))
    private_key = RSA.construct((n, d))
    key_pair = RSA.construct((n, e, d,))
    print("PublicKey: ", public_key)
    print("-----------------------")
    print("PrivateKey: ", key_pair)
    print("-----------------------")
    print("Original message: ", message)
    print("-----------------------")
    encryptor = PKCS1_OAEP.new(public_key)
    m_encrypted = encryptor.encrypt(message)
    print("Encrypted message: ", m_encrypted,"\n")
    print("-----------------------")
    decryptor = PKCS1_OAEP.new(key_pair)
    m_decrypted = decryptor.decrypt(m_encrypted)
    print("Decrypted message: ", m_decrypted)
    print("-----------------------")

    # m_encrypted = RSA_encrypt(message, e, n)
    # print("Message: ", message)
    # print("RSA_encrypt: ", m_encrypted)
    # print("RSA_decrypt: ", RSA_decrypt(m_encrypted, d, n))