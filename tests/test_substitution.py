# tests/test_substitution.py
import string
from src.ciphers import substitution, caesar

def test_permutation_roundtrip():
    plaintext = "HelloWorld"
    key = "zyxwvutsrqponmlkjihgfedcba"  # reverse alphabet
    ct = substitution.permutation_cipher_encrypt(plaintext, key)
    pt = substitution.permutation_cipher_decrypt(ct, key)
    # permutation functions lower-case and operate on letters; compare lower()
    assert pt.lower() == plaintext.lower()

def test_substitution_caesar_wrapper():
    plaintext = "abcXYZ"
    k = 4
    ct = substitution.caesar_encrypt(plaintext, k)
    pt = substitution.caesar_decrypt(ct, k)
    assert pt == plaintext

def test_substitution_alias_encrypt_decrypt():
    # if module exposes encrypt/decrypt aliases they should behave for permutation keys
    if hasattr(substitution, "encrypt") and hasattr(substitution, "decrypt"):
        key = "zyxwvutsrqponmlkjihgfedcba"
        ct = substitution.encrypt("AttackAtDawn", key)
        assert substitution.decrypt(ct, key).lower() == "attackatdawn"
