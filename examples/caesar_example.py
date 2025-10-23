# examples/caesar_example.py
from src.ciphers import caesar

if __name__ == '__main__':
    text = \"Hello World!\"
    key = 3
    ct = caesar.encrypt(text, key)
    print(f\"Plaintext: {text}\")
    print(f\"Ciphertext: {ct}\")
    print(f\"Decrypted: {caesar.decrypt(ct, key)}\")

