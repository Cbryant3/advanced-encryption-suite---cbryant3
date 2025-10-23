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

# Main function 
def main():
    while True:
        print("\nChoose an option:")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Brute Force Attack")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ") #user inputs number for option

        if choice == '1':
            plaintext = input("Enter plaintext: ")
            key = int(input("Enter key (numeric): "))
            ciphertext = encrypt(plaintext, key)
            print(f"Ciphertext: {ciphertext}")
        elif choice == '2':
            ciphertext = input("Enter ciphertext: ")
            key = int(input("Enter key (numeric): "))
            plaintext = decrypt(ciphertext, key)
            print(f"Decrypted plaintext: {plaintext}")
        elif choice == '3':
            ciphertext = input("Enter ciphertext: ")
            brute_force_attack(ciphertext)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

