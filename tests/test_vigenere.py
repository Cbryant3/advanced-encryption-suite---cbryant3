# tests/test_vigenere.py
from src.ciphers import vigenere

def test_vigenere_roundtrip_simple():
    plaintext = "AttackAtDawn"
    key = "LEMON"
    ct = vigenere.vigenere_cipher_encrypt(plaintext, key)
    pt = vigenere.vigenere_cipher_decrypt(ct, key)
    assert pt == plaintext

def test_vigenere_aliases():
    if hasattr(vigenere, "encrypt") and hasattr(vigenere, "decrypt"):
        plaintext = "HelloVig"
        key = "KEY"
        ct = vigenere.encrypt(plaintext, key)
        assert vigenere.decrypt(ct, key) == plaintext
