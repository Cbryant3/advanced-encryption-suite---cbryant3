# src/hashing/sha_simple.py
import hashlib

# My name
name = "Cameron Bryant"

def run():
    # Compute SHA-256 hash
    hash_value = hashlib.sha256(name.encode()).hexdigest()

    # Print the hash value in hexadecimal
    print(f"SHA-256 hash of '{name}': {hash_value}")


if __name__ == "__main__":
    run()

