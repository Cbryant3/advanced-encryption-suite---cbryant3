# src/modes/modes.py
#Thin convenience wrappers for encryption modes.
from Crypto.Cipher import AES, DES, DES3
from src.symmetric.aes_des import encrypt_with_mode, decrypt_with_mode

ALGO_MAP = {
    'AES': AES,
    'DES': DES,
    '3DES': DES3
}

MODE_MAP = {
    1: 'ECB',
    2: 'CBC',
    3: 'CFB'
}

def encrypt(algorithm_name, plaintext, key, mode_choice, block_size):
    algorithm = ALGO_MAP[algorithm_name]
    mode_const = {1: algorithm.MODE_ECB, 2: algorithm.MODE_CBC, 3: algorithm.MODE_CFB}[mode_choice]
    return encrypt_with_mode(algorithm, plaintext, key, mode_const, block_size)

def decrypt(algorithm_name, ciphertext_bytes, key, mode_choice, block_size):
    algorithm = ALGO_MAP[algorithm_name]
    mode_const = {1: algorithm.MODE_ECB, 2: algorithm.MODE_CBC, 3: algorithm.MODE_CFB}[mode_choice]
    return decrypt_with_mode(algorithm, ciphertext_bytes, key, mode_const, block_size)

