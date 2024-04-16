#for more info, and seeing Encryption and decryption working together go to: https://replit.com/join/rhmcdwnovc-thomasweis1

from base64 import b64decode
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def decrypt(enc_dict, password):
    # decode the dictionary entries from base64
    salt = b64decode(enc_dict['salt'])
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])

    # generate the private key from the password and salt
    private_key = hashlib.scrypt(password.encode(),
                                 salt=salt,
                                 n=2**14,
                                 r=8,
                                 p=1,
                                 dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)
    
    return decrypted
