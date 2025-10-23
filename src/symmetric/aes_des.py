# src/symmetric/aes_des.py
#AES/DES/3DES functions (moved from assignment 2).

import os
from Crypto.Cipher import AES, DES, DES3
from Crypto.Util.Padding import pad, unpad

BLOCK_SIZE_AES = 16
BLOCK_SIZE_DES = 8

def aes_encrypt(plaintext, key, mode):
    if mode == AES.MODE_ECB:
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    else:
        iv = os.urandom(AES.block_size)
        cipher = AES.new(key, mode, iv)
        return iv + cipher.encrypt(pad(plaintext.encode(), AES.block_size))  # Prepend IV

def aes_decrypt(ciphertext, key, mode):
    if mode == AES.MODE_ECB:
        cipher = AES.new(key, AES.MODE_ECB)
        return unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')
    else:
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, mode, iv)
        return unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size).decode('utf-8')

def encrypt_with_mode(algorithm, plaintext, key, mode, block_size):
    if mode == algorithm.MODE_ECB:
        cipher = algorithm.new(key, mode)
        return cipher.encrypt(pad(plaintext.encode(), block_size))
    else:
        iv = os.urandom(block_size)
        cipher = algorithm.new(key, mode, iv)
        return iv + cipher.encrypt(pad(plaintext.encode(), block_size))

def decrypt_with_mode(algorithm, ciphertext, key, mode, block_size):
    if mode == algorithm.MODE_ECB:
        cipher = algorithm.new(key, mode)
        return unpad(cipher.decrypt(ciphertext), block_size).decode('utf-8')
    else:
        iv = ciphertext[:block_size]
        cipher = algorithm.new(key, mode, iv)
        return unpad(cipher.decrypt(ciphertext[block_size:]), block_size).decode('utf-8')

