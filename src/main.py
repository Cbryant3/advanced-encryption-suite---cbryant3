# src/main.py
"""Top-level entrypoint for the project. Keeps menu minimal and delegates to modules."""

from src.ciphers import caesar, substitution, transposition, vigenere
from src.symmetric import aes_des
from src.utils.helpers import get_menu_choice
from src.hashing import sha_simple, sha_stats
from src.modes import modes

def print_main_menu():
    print("""Main Menu:
1. Caesar Cipher
2. Substitution Cipher
3. Transposition Ciphers
4. Vigenère Cipher
5. Encryption Algorithms (AES/DES/3DES)
6. Examples
7. Exit
""")


def handle_caesar():
    print("Caesar Cipher")
    action = get_menu_choice("1. Encrypt\n2. Decrypt\n3. Brute Force Attack\n4.Back\nChoose: ", 1, 4)
    if action == 4:
        return

    if action == 1:
        text = input("Enter text: ")
        key = int(input("Enter key (integer shift): "))
        encrypted = caesar.encrypt(text, key)
        print(f"Encrypted: {encrypted}")
    elif action == 2:
        text = input("Enter ciphertext: ")
        key = int(input("Enter key (integer shift): "))
        decrypted = caesar.decrypt(text, key)
        print(f"Decrypted: {decrypted}")
    else:  # action == 3: brute force
        ciphertext = input("Enter ciphertext for brute-force: ")
        print("Trying all possible keys (1-25):")
        caesar.brute_force_attack(ciphertext)


def handle_symmetric_encryption():
    # Select algorithm
    print("Select algorithm:\n1. AES\n2. DES\n3. 3DES\n4. Back")
    algo_choice = get_menu_choice("Choose (1-4): ", 1, 4)
    if algo_choice == 4:
        return

    algo_map = {1: 'AES', 2: 'DES', 3: '3DES'}
    algorithm_name = algo_map[algo_choice]

    # Default keys
    default_keys = {
        'AES': aes_des.DEFAULT_AES_KEY,
        'DES': aes_des.DEFAULT_DES_KEY,
        '3DES': aes_des.DEFAULT_3DES_KEY
    }
    key = default_keys[algorithm_name]

    # Select mode
    print("Select mode:\n1. ECB\n2. CBC\n3. CFB\n4. Back")
    mode_choice = get_menu_choice("Choose (1-4): ", 1, 4)
    if mode_choice == 4:
        return

    # Encrypt/Decrypt
    print("1. Encrypt\n2. Decrypt\n3. Back")
    action_choice = get_menu_choice("Choose (1-3): ", 1, 3)
    if action_choice == 3:
        return

    block_size = aes_des.BLOCK_SIZE_AES if algorithm_name == 'AES' else aes_des.BLOCK_SIZE_DES

    if action_choice == 1:
        plaintext = input("Enter plaintext: ")
        ciphertext = modes.encrypt(algorithm_name, plaintext, key, mode_choice, block_size)
        print(f"Encrypted (hex): {ciphertext.hex()}")
    else:
        ciphertext_hex = input("Enter ciphertext (hex): ")
        ciphertext_bytes = bytes.fromhex(ciphertext_hex)
        plaintext = modes.decrypt(algorithm_name, ciphertext_bytes, key, mode_choice, block_size)
        print(f"Decrypted: {plaintext}")

def handle_substitution():
    print("Substitution Cipher")
    print("1. Caesar Cipher")
    print("2. Permutation Cipher")
    print("3. Back")
    choice = get_menu_choice("Choose: ", 1, 3)
    if choice == 3:
        return

    text = input("Enter text: ")

    if choice == 1:  # Caesar
        key = int(input("Enter key (integer shift): "))
        action = get_menu_choice("1. Encrypt\n2. Decrypt\n3. Back\nChoose: ", 1, 3)
        if action == 3:
            return
        if action == 1:
            print(f"Encrypted: {substitution.caesar_encrypt(text, key)}")
        else:
            print(f"Decrypted: {substitution.caesar_decrypt(text, key)}")
    else:  # Permutation
        default = ''.join(chr(i) for i in range(ord('a'), ord('z')+1))  # 'abcdefghijklmnopqrstuvwxyz'
        key = input(f"Enter 26-letter key (or leave blank for default {default}): ") or default
        if len(key) != 26:
            print("Key must be exactly 26 letters!")
            return
        action = get_menu_choice("1. Encrypt\n2. Decrypt\n3. Back\nChoose: ", 1, 3)
        if action == 3:
            return
        if action == 1:
            print(f"Encrypted: {substitution.permutation_cipher_encrypt(text, key)}")
        else:
            print(f"Decrypted: {substitution.permutation_cipher_decrypt(text, key)}")

def handle_transposition():
    print("Transposition Cipher")
    action = get_menu_choice(
        "1. Simple Encrypt\n"
        "2. Simple Decrypt\n"
        "3. Double Encrypt\n"
        "4. Double Decrypt\n"
        "5. Back\nChoose: ", 1, 5
    )

    if action == 5:
        return

    text = input("Enter text: ")

    # SIMPLE TRANSPOSITION
    if action in (1, 2):
        key = int(input("Enter key (integer): "))
        if action == 1:
            encrypted = transposition.simple_transposition_encrypt(text, key)
            print(f"Encrypted: {encrypted}")
        else:
            decrypted = transposition.simple_transposition_decrypt(text, key)
            print(f"Decrypted: {decrypted}")

    # DOUBLE TRANSPOSITION
    elif action in (3, 4):
        key1 = int(input("Enter first key (integer): "))
        key2 = int(input("Enter second key (integer): "))
        if action == 3:
            encrypted = transposition.double_transposition_encrypt(text, key1, key2)
            print(f"Double Encrypted: {encrypted}")
        else:
            decrypted = transposition.double_transposition_decrypt(text, key1, key2)
            print(f"Double Decrypted: {decrypted}")


def handle_vigenere():
    print("Vigenère Cipher")
    action = get_menu_choice("1. Encrypt\n2. Decrypt\n3. Back\nChoose: ", 1, 3)
    if action == 3:
        return
    text = input("Enter text: ")
    key = input("Enter keyword: ")
    if action == 1:
        encrypted = vigenere.encrypt(text, key)
        print(f"Encrypted: {encrypted}")
    else:
        decrypted = vigenere.decrypt(text, key)
        print(f"Decrypted: {decrypted}")

def main():
    while True:
        print_main_menu()
        choice = get_menu_choice("Choose an option (1-7): ", 1, 7)
        
        if choice == 1:
            handle_caesar()
        elif choice == 2:
            handle_substitution()
        elif choice == 3:
            handle_transposition()
        elif choice == 4:
            handle_vigenere()
        elif choice == 5:
            handle_symmetric_encryption()
        elif choice == 6:
            print("1. Simple SHA-256 example\n2. SHA-256 statistics")
            sub = get_menu_choice("Choose (1-2): ", 1, 2)
            if sub == 1:
                sha_simple.run()
            else:
                n = int(input("Number of inputs to hash (default 10000): ") or "10000")
                plot = input("Show plot? (y/n): ").strip().lower().startswith("y")
                sha_stats.run(num_inputs=n, plot=plot)
        else:  # choice == 7
            print("Exiting program. Goodbye!")
            break

if __name__ == '__main__':
    main()


