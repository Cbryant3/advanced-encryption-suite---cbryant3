# src/ciphers/caesar.py
# Caesar Cipher Encryption, Decryption, and Brute Force Attack

# Function to encrypt plaintext using a shift key
def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a')) #Lower-case handling
            else:
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A')) #Upper-case handling
        else:
            ciphertext += char  # Non-alphabetics stay the same
    return ciphertext

# Function to decrypt ciphertext using a shift key
def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)  # Reverse the shift for decryption

# Function to perform a brute force attack on the ciphertext
def brute_force_attack(ciphertext):
    print("Brute force attack results:")
    for key in range(1, 26): #Try every possible combination of ciphertext and key
        possible_plaintext = decrypt(ciphertext, key)
        print(f"Key = {key}: {possible_plaintext}")

encrypt = encrypt  
decrypt = decrypt  
brute_force = brute_force_attack

