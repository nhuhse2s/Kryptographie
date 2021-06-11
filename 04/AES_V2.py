#####
##
#####

import hashlib
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

#####

cipher_key  = "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c" ## 16 Byte
plaintext   = "32 43 f6 a8 88 5a 30 8d 31 31 98 a2 e0 37 07 34"
output      = "39 25 84 1d 02 dc 09 fb dc 11 85 97 19 6a 0b 32"
iv          = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"

key1 = bytes.fromhex('2b7e151628aed2a6abf7158809cf4f3c')
plaintext1 = bytes.fromhex('3243f6a8885a308d313198a2e0370734')
iv1 = bytes.fromhex('00000000000000000000000000000000')

def check():
    ##key = hashlib.sha256(cipher_key.encode()).digest()
    cipher = AES.new(key1, AES.MODE_CBC, iv1)
    padded_plaintext = padding(plaintext)
    cipher_text = cipher.encrypt(plaintext1)

    print("###########################")
    print(cipher_text.hex())
    print("###########################")

def padding(plaintext):

    number_of_bytes_to_pad = AES.block_size - len(plaintext) % AES.block_size
    ascii_string = chr(number_of_bytes_to_pad)
    padding_str = number_of_bytes_to_pad * ascii_string
    padded_plain_text = plaintext + padding_str

    return padded_plain_text

if __name__ == "__main__":
    check()
