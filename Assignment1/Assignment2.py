import string
import math
from Crypto.Cipher import AES, DES, DES3
from Crypto.Util.Padding import pad, unpad
import os

# Default keys
DEFAULT_VIGENERE_KEY = "defaultkey"
DEFAULT_TRANS_KEY = 5
DEFAULT_DOUBLE_TRANS_KEY1 = 5
DEFAULT_DOUBLE_TRANS_KEY2 = 7
DEFAULT_SHIFT_KEY = 3
DEFAULT_PERMUTATION_KEY = "zyxwvutsrqponmlkjihgfedcba"  # Adjusted for uniqueness
DEFAULT_AES_KEY = os.urandom(16)  # 128-bit key for AES
DEFAULT_DES_KEY = os.urandom(8)    # 64-bit key for DES
DEFAULT_3DES_KEY = os.urandom(24)  # 168-bit key for 3DES
BLOCK_SIZE_AES = 16
BLOCK_SIZE_DES = 8

# Menu definitions
def print_main_menu():
    print("\nMain Menu:")
    print("1. Substitution Ciphers")
    print("2. Transposition Ciphers")
    print("3. Vigenère Cipher")
    print("4. Encryption Algorithms (AES-128, DES, 3DES)")
    print("5. Encryption Modes (ECB, CBC, CFB, OFB) - Not Implemented")
    print("6. Exit")

def print_substitution_menu():
    print("\nSubstitution Ciphers:")
    print("1. Shift Cipher (Caesar Cipher)")
    print("2. Permutation Cipher")
    print("3. Back to Main Menu")

def print_transposition_menu():
    print("\nTransposition Ciphers:")
    print("1. Simple Transposition Cipher")
    print("2. Double Transposition Cipher")
    print("3. Back to Main Menu")

def print_vigenere_menu():
    print("\nVigenère Cipher:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Back to Main Menu")

def print_encryption_algorithms_menu():
    print("\nEncryption Algorithms:")
    print("1. AES-128")
    print("2. DES")
    print("3. 3DES")
    print("4. Back to Main Menu")

def print_encrypt_decrypt_menu():
    print("\nSelect an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Back to Previous Menu")

def print_encryption_modes_menu():
    print("\nEncryption Modes:")
    print("1. ECB (Electronic Codebook)")
    print("2. CBC (Cipher Block Chaining)")
    print("3. CFB (Cipher Feedback)")
    print("4. Back to Encryption Algorithms")


# Get user menu choice with validation
def get_menu_choice(prompt, min_val, max_val):
    while True:
        try:
            choice = int(input(prompt))
            if min_val <= choice <= max_val:
                return choice
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Prompt for key selection: default or custom
def use_default_key():
    while True:
        use_default = input("Do you want to use the default key? (y/n): ").strip().lower()
        if use_default in ['y', 'n']:
            return use_default == 'y'
        print("Please enter 'y' for yes or 'n' for no.")

# Cipher Implementations

# Shift Cipher (Caesar Cipher) - Encryption and Decryption
def caesar_cipher_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

# Permutation Cipher - Encryption and Decryption
def permutation_cipher_encrypt(plaintext, key):
    alphabet = string.ascii_lowercase
    key_map = {alphabet[i]: key[i] for i in range(26)}
    encrypted_text = ''.join(key_map.get(char, char) for char in plaintext.lower())
    return encrypted_text

def permutation_cipher_decrypt(ciphertext, key):
    alphabet = string.ascii_lowercase
    reverse_key_map = {key[i]: alphabet[i] for i in range(26)}
    decrypted_text = ''.join(reverse_key_map.get(char, char) for char in ciphertext.lower())
    return decrypted_text

# Handle Substitution Cipher
def handle_substitution_cipher():
    default_shift = DEFAULT_SHIFT_KEY
    default_permutation_key = DEFAULT_PERMUTATION_KEY

    while True:
        print_substitution_menu()
        sub_choice = get_menu_choice("Select a substitution cipher (1-3): ", 1, 3)

        if sub_choice == 1:  # Shift Cipher
            print_encrypt_decrypt_menu()
            action_choice = get_menu_choice("Choose (1-3): ", 1, 3)

            if action_choice == 1:  # Encrypt
                plaintext = input("Enter the plaintext: ")
                shift = default_shift if use_default_key() else int(input("Enter the shift value (0-25): "))
                encrypted = caesar_cipher_encrypt(plaintext, shift)
                print(f"Encrypted Text (Shift Cipher): {encrypted}")

            elif action_choice == 2:  # Decrypt
                ciphertext = input("Enter the ciphertext: ")
                shift = default_shift if use_default_key() else int(input("Enter the shift value (0-25): "))
                decrypted = caesar_cipher_decrypt(ciphertext, shift)
                print(f"Decrypted Text (Shift Cipher): {decrypted}")

        elif sub_choice == 2:  # Permutation Cipher
            print_encrypt_decrypt_menu()
            action_choice = get_menu_choice("Choose (1-3): ", 1, 3)

            if action_choice == 1:  # Encrypt
                plaintext = input("Enter the plaintext: ")
                key = default_permutation_key if use_default_key() else input("Enter the 26-letter permutation key (lowercase letters only): ").lower()

                if len(key) != 26 or not all(c in string.ascii_lowercase for c in key) or len(set(key)) != 26:
                    print("Error: Key must be exactly 26 unique lowercase letters.")
                    continue

                encrypted = permutation_cipher_encrypt(plaintext, key)
                print(f"Encrypted Text (Permutation Cipher): {encrypted}")

            elif action_choice == 2:  # Decrypt
                ciphertext = input("Enter the ciphertext: ")
                key = default_permutation_key if use_default_key() else input("Enter the 26-letter permutation key (lowercase letters only): ").lower()

                if len(key) != 26 or not all(c in string.ascii_lowercase for c in key) or len(set(key)) != 26:
                    print("Error: Key must be exactly 26 unique lowercase letters.")
                    continue

                decrypted = permutation_cipher_decrypt(ciphertext, key)
                print(f"Decrypted Text (Permutation Cipher): {decrypted}")
        else:
            break

# Simple Transposition Cipher - Encryption and Decryption
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

# Double Transposition Cipher - Encryption and Decryption
def double_transposition_encrypt(plaintext, key1, key2):
    first_encryption = simple_transposition_encrypt(plaintext, key1)
    return simple_transposition_encrypt(first_encryption, key2)

def double_transposition_decrypt(ciphertext, key1, key2):
    first_decryption = simple_transposition_decrypt(ciphertext, key2)
    return simple_transposition_decrypt(first_decryption, key1)

# Handle Transposition Cipher
def handle_transposition_cipher():
    while True:
        print_transposition_menu()
        trans_choice = get_menu_choice("Select a transposition cipher (1-3): ", 1, 3)

        if trans_choice == 1:  # Simple Transposition Cipher
            print_encrypt_decrypt_menu()
            action_choice = get_menu_choice("Choose (1-3): ", 1, 3)

            if action_choice == 1:  # Encrypt
                plaintext = input("Enter the plaintext: ")
                key = DEFAULT_TRANS_KEY if use_default_key() else int(input("Enter the transposition key: "))
                encrypted = simple_transposition_encrypt(plaintext, key)
                print(f"Encrypted Text (Simple Transposition Cipher): {encrypted}")

            elif action_choice == 2:  # Decrypt
                ciphertext = input("Enter the ciphertext: ")
                key = DEFAULT_TRANS_KEY if use_default_key() else int(input("Enter the transposition key: "))
                decrypted = simple_transposition_decrypt(ciphertext, key)
                print(f"Decrypted Text (Simple Transposition Cipher): {decrypted}")

        elif trans_choice == 2:  # Double Transposition Cipher
            print_encrypt_decrypt_menu()
            action_choice = get_menu_choice("Choose (1-3): ", 1, 3)

            if action_choice == 1:  # Encrypt
                plaintext = input("Enter the plaintext: ")
                key1 = DEFAULT_DOUBLE_TRANS_KEY1 if use_default_key() else int(input("Enter the first transposition key: "))
                key2 = DEFAULT_DOUBLE_TRANS_KEY2 if use_default_key() else int(input("Enter the second transposition key: "))
                encrypted = double_transposition_encrypt(plaintext, key1, key2)
                print(f"Encrypted Text (Double Transposition Cipher): {encrypted}")

            elif action_choice == 2:  # Decrypt
                ciphertext = input("Enter the ciphertext: ")
                key1 = DEFAULT_DOUBLE_TRANS_KEY1 if use_default_key() else int(input("Enter the first transposition key: "))
                key2 = DEFAULT_DOUBLE_TRANS_KEY2 if use_default_key() else int(input("Enter the second transposition key: "))
                decrypted = double_transposition_decrypt(ciphertext, key1, key2)
                print(f"Decrypted Text (Double Transposition Cipher): {decrypted}")

        else:
            break

# Vigenère Cipher - Encryption
def vigenere_cipher_encrypt(plaintext, key):
    key = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    encrypted_text = []
    
    for p, k in zip(plaintext, key):
        if p.isalpha():
            shift = ord(k.lower()) - ord('a')
            base = ord('A') if p.isupper() else ord('a')
            encrypted_text.append(chr((ord(p) - base + shift) % 26 + base))
        else:
            encrypted_text.append(p)  # Non-alphabetic characters remain unchanged
    
    return ''.join(encrypted_text)

# Vigenère Cipher - Decryption
def vigenere_cipher_decrypt(ciphertext, key):
    key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    decrypted_text = []
    
    for c, k in zip(ciphertext, key):
        if c.isalpha():
            shift = ord(k.lower()) - ord('a')
            base = ord('A') if c.isupper() else ord('a')
            decrypted_text.append(chr((ord(c) - base - shift + 26) % 26 + base))
        else:
            decrypted_text.append(c)  # Non-alphabetic characters remain unchanged
    
    return ''.join(decrypted_text)

# Handle Vigenère Cipher
def handle_vigenere_cipher():
    while True:
        print_vigenere_menu()
        vig_choice = get_menu_choice("Select (1-3): ", 1, 3)

        if vig_choice == 1:  # Encrypt
            plaintext = input("Enter the plaintext: ")
            key = DEFAULT_VIGENERE_KEY if use_default_key() else input("Enter the key: ")
            encrypted = vigenere_cipher_encrypt(plaintext, key)
            print(f"Encrypted Text (Vigenère Cipher): {encrypted}")

        elif vig_choice == 2:  # Decrypt
            ciphertext = input("Enter the ciphertext: ")
            key = DEFAULT_VIGENERE_KEY if use_default_key() else input("Enter the key: ")
            decrypted = vigenere_cipher_decrypt(ciphertext, key)
            print(f"Decrypted Text (Vigenère Cipher): {decrypted}")

        else:
            break

# AES encryption with modes
def aes_encrypt(plaintext, key, mode):
    if mode == AES.MODE_ECB:
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    else:
        iv = os.urandom(AES.block_size)
        cipher = AES.new(key, mode, iv)
        return iv + cipher.encrypt(pad(plaintext.encode(), AES.block_size))  # Prepend IV

# AES decryption with modes
def aes_decrypt(ciphertext, key, mode):
    if mode == AES.MODE_ECB:
        cipher = AES.new(key, AES.MODE_ECB)
        return unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')
    else:
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, mode, iv)
        return unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size).decode('utf-8')





# Handle Encryption Algorithms
def handle_encryption_algorithms():
    while True:
        print_encryption_algorithms_menu()
        algo_choice = get_menu_choice("Select an encryption algorithm (1-4): ", 1, 4)

        if algo_choice == 1:  # AES
            key = DEFAULT_AES_KEY
            handle_encryption_modes(AES, key, BLOCK_SIZE_AES)

        elif algo_choice == 2:  # DES
            key = DEFAULT_DES_KEY
            handle_encryption_modes(DES, key, BLOCK_SIZE_DES)

        elif algo_choice == 3:  # 3DES
            key = DEFAULT_3DES_KEY
            handle_encryption_modes(DES3, key, BLOCK_SIZE_DES)

        else:
            break


# Generic encryption for AES, DES, and 3DES with modes
def encrypt_with_mode(algorithm, plaintext, key, mode, block_size):
    if mode == algorithm.MODE_ECB:
        cipher = algorithm.new(key, mode)
        return cipher.encrypt(pad(plaintext.encode(), block_size))
    else:
        iv = os.urandom(block_size)  # IV needed for modes like CBC, CFB, OFB
        cipher = algorithm.new(key, mode, iv)
        return iv + cipher.encrypt(pad(plaintext.encode(), block_size))  

# Generic decryption for AES, DES, and 3DES with modes
def decrypt_with_mode(algorithm, ciphertext, key, mode, block_size):
    if mode == algorithm.MODE_ECB:
        cipher = algorithm.new(key, mode)
        return unpad(cipher.decrypt(ciphertext), block_size).decode('utf-8')
    else:
        iv = ciphertext[:block_size]
        cipher = algorithm.new(key, mode, iv)
        return unpad(cipher.decrypt(ciphertext[block_size:]), block_size).decode('utf-8')

# Handle Encryption Modes
def handle_encryption_modes(algorithm, key, block_size):
    while True:
        print_encryption_modes_menu()
        mode_choice = get_menu_choice("Select an encryption mode (1-4): ", 1, 4)

        if mode_choice == 1:  # ECB
            mode = algorithm.MODE_ECB
        elif mode_choice == 2:  # CBC
            mode = algorithm.MODE_CBC
        elif mode_choice == 3:  # CFB
            mode = algorithm.MODE_CFB
        else:
            break  # Go back to previous menu

        print_encrypt_decrypt_menu()
        action_choice = get_menu_choice("Choose (1-3): ", 1, 3)

        if action_choice == 1:  # Encrypt
            plaintext = input("Enter the plaintext: ")
            encrypted = encrypt_with_mode(algorithm, plaintext, key, mode, block_size)
            print(f"Encrypted Text ({algorithm.__name__} - Mode {mode_choice}): {encrypted.hex()}")  # Show as hex

        elif action_choice == 2:  # Decrypt
            ciphertext = input("Enter the ciphertext (hex format): ")
            decrypted = decrypt_with_mode(algorithm, bytes.fromhex(ciphertext), key, mode, block_size)
            print(f"Decrypted Text ({algorithm.__name__} - Mode {mode_choice}): {decrypted}")
        else:
            break


# Main loop
def main():
    while True:
        print_main_menu()
        choice = get_menu_choice("Choose an option (1-6): ", 1, 6)

        if choice == 1:  # Substitution Ciphers
            handle_substitution_cipher()
        elif choice == 2:  # Transposition Ciphers
            handle_transposition_cipher()
        elif choice == 3:  # Vigenère Cipher
            handle_vigenere_cipher()
        elif choice == 4: # Encryption Algorithms (AES-128, DES, 3DES)
            handle_encryption_algorithms()
        elif choice == 5:  # Exit
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Feature not implemented yet.")

if __name__ == "__main__":
    main()
