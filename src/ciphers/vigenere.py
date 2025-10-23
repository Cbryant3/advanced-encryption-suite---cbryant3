# src/ciphers/vigenere.py
#Vigenère cipher functions (preserve original names)

from src.utils.helpers import DEFAULT_VIGENERE_KEY

def vigenere_cipher_encrypt(plaintext, key):
    key = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    encrypted_text = []
    for p, k in zip(plaintext, key):
        if p.isalpha():
            shift = ord(k.lower()) - ord('a')
            base = ord('A') if p.isupper() else ord('a')
            encrypted_text.append(chr((ord(p) - base + shift) % 26 + base))
        else:
            encrypted_text.append(p)
    return ''.join(encrypted_text)

def vigenere_cipher_decrypt(ciphertext, key):
    key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    decrypted_text = []
    for c, k in zip(ciphertext, key):
        if c.isalpha():
            shift = ord(k.lower()) - ord('a')
            base = ord('A') if c.isupper() else ord('a')
            decrypted_text.append(chr((ord(c) - base - shift + 26) % 26 + base))
        else:
            decrypted_text.append(c)
    return ''.join(decrypted_text)

# Default aliases for main.py
encrypt = vigenere_cipher_encrypt
decrypt = vigenere_cipher_decrypt
