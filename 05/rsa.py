from Crypto.Util import number
from timeit import default_timer as timer

def RSA_a():  
    prime_length = 1500
    for x in range(0,10):
        start = timer()
        prime_number = number.getPrime(prime_length)
        end = timer()
        print("x: ", x, "| time: ", end - start, " Sekunden")

def RSA_b():
    prime_length = 3000
    # prime_p      = number.getPrime(prime_length)    ##5
    # prime_q      = number.getPrime(prime_length)    ##11
    # n            = prime_p*prime_q                  ##55
    # phi_n        = (prime_p-1)*(prime_q-1)          ##40
    # e            = (2**16) + 1                      ##17
    # d            = modinv(e, phi_n)                 ##33

    prime_p      = 5    
    prime_q      = 11    
    n            = 55                 
    phi_n        = 40         
    e            = 17                      
    d            = modinv(e, phi_n)                 
    return (n, e, d)

def RSA_encrypt(x, e, n):
    return (x**e)%n

def RSA_decrypt(x, d, n):
    return (x**d)%n

def modinv(e, phi):
    d_old = 0; r_old = phi
    d_new = 1; r_new = e
    while r_new > 0:
        a = r_old // r_new
        (d_old, d_new) = (d_new, d_old - a * d_new)
        (r_old, r_new) = (r_new, r_old - a * r_new)
    return d_old % phi if r_old == 1 else None

if __name__ == "__main__":
    #RSA_a()
    
    n, e, d = RSA_b()
    message = 30
    m_encrypted = RSA_encrypt(message, e, n)
    
    print("Message: ", message)
    print("RSA_encrypt: ", m_encrypted)
    print("RSA_decrypt: ", RSA_decrypt(m_encrypted, d, n))