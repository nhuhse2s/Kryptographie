#######################
### AES Brute Force ###
#######################

import binascii
from Crypto.Cipher import AES

def crack(key: str, chiffre, iv: str):

    #key_list = [0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    sub_key = ""
    tmp_x_1 = ""
    tmp_x_2 = ""

    for x_1 in range(0,256):
        for x_2 in range(0, 256):

            #sub_key = "" + str(x_1) + str(x_2) + str(x_3) + str(x_4)
            tmp_x_1 = bytes.fromhex(str(x_1))
            tmp_x_2 = bytes.fromhex(str(x_2))
                    
            sub_key += "" + tmp_x_1 + tmp_x_2
            #sum_key = sub_key + bytes.fromhex(key)
            sum_key = sub_key + key
            sum_key_bytes = bytes.fromhex(sum_key)
            print(sum_key)
            aes_cipher = AES.new(sum_key_bytes, AES.MODE_CBC, iv_bytes)
            decrypted_text = aes_cipher.decrypt(chiffre)
                    
            if(decrypted_text.startswith(b'25 50 44 46 2D')):
                print("found")
    return None

if __name__ == "__main__":

    chiffre = open("chiffrat_AES.bin", "rb").read()
    key     = '5555555555555555555555555555'
    key_x   = "00 00 55 55 55 55 55 55 55 55 55 55 55 55 55 55"
    iv      = "80 81 82 83 84 85 86 87 88 89 8a 8b 8c 8d 8e 8f"
    iv_bytes = bytes.fromhex('808182838485868788898a8b8c8d8e8f')

    #print(bytes(32).hex())
    #print(hex(1))
    #print("" + str(0) + str(0) + str(0) + str(0) + key)
    print(crack(key, chiffre, iv_bytes))
    