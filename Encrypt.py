#for more info, and seeing Encryption and decryption working together go to: https://replit.com/join/rhmcdwnovc-thomasweis1

#pip install pycryptodomex

from base64 import b64encode
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt(plain_text, password):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(password.encode(),
                                 salt=salt,
                                 n=2**14,
                                 r=8,
                                 p=1,
                                 dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(
        bytes(plain_text, 'utf-8'))
    return {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }

