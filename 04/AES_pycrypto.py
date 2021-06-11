import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]

# def AESObject(key, plaintext):
#     m_key = key
#     m_plaintext = plaintext

class AESObject(object):
    def __init__(self, key, plaintext):
        self.key = key
        self.plaintext = plaintext

def Main():
    print("Test")

    cipher_key  = "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c"
    plaintext   = "32 43 f6 a8 88 5a 30 8d 31 31 98 a2 e0 37 07 34"
    output      = "39 02 dc 19 25 dc 11 6a 84 09 85 0b 1d fb 97 32"

    aes_c = AESCipher((cipher_key))
    enc = aes_c.encrypt(plaintext)
    print(aes_c.key)
    print(enc)
    
    
if __name__ == "__main__":
    Main()