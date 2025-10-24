# src/ciphers/substitution.py
import string
from src.utils.helpers import DEFAULT_PERMUTATION_KEY, use_default_key
from src.ciphers import caesar

def permutation_cipher_encrypt(plaintext, key):
    alphabet = string.ascii_lowercase
    key = key.lower()  # standardize
    key_map = {alphabet[i]: key[i] for i in range(26)}
    return ''.join(key_map.get(char, char) for char in plaintext.lower())

def permutation_cipher_decrypt(ciphertext, key):
    alphabet = string.ascii_lowercase
    key = key.lower()  # standardize
    # Create reverse mapping: cipher letter → original letter
    reverse_key_map = {key[i]: alphabet[i] for i in range(26)}
    return ''.join(reverse_key_map.get(char, char) for char in ciphertext.lower())

# Thin wrappers for Caesar (optional)
def caesar_encrypt(plaintext, shift):
    return caesar.encrypt(plaintext, shift)

def caesar_decrypt(ciphertext, shift):
    return caesar.decrypt(ciphertext, shift)

encrypt = permutation_cipher_encrypt
decrypt = permutation_cipher_decrypt
