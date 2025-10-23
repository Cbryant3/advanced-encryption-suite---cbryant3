# src/ciphers/transposition.py
#Simple and double transposition ciphers.

import math
from src.utils.helpers import DEFAULT_TRANS_KEY, DEFAULT_DOUBLE_TRANS_KEY1, DEFAULT_DOUBLE_TRANS_KEY2

def simple_transposition_encrypt(plaintext, key):
    ciphertext = [''] * key
    for column in range(key):
        current_index = column
        while current_index < len(plaintext):
            ciphertext[column] += plaintext[current_index]
            current_index += key
    return ''.join(ciphertext)

def simple_transposition_decrypt(ciphertext, key):
    num_of_columns = math.ceil(len(ciphertext) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(ciphertext)

    plaintext = [''] * num_of_columns
    column = 0
    row = 0

    for symbol in ciphertext:
        plaintext[column] += symbol
        column += 1
        if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            column = 0
            row += 1

    return ''.join(plaintext)

def double_transposition_encrypt(plaintext, key1, key2):
    first_encryption = simple_transposition_encrypt(plaintext, key1)
    return simple_transposition_encrypt(first_encryption, key2)

def double_transposition_decrypt(ciphertext, key1, key2):
    first_decryption = simple_transposition_decrypt(ciphertext, key2)
    return simple_transposition_decrypt(first_decryption, key1)


# Default aliases for main.py
encrypt = simple_transposition_encrypt
decrypt = simple_transposition_decrypt

double_encrypt = double_transposition_encrypt
double_decrypt = double_transposition_decrypt
