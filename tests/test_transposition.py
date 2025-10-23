# tests/test_transposition.py
from src.ciphers import transposition

def test_simple_transposition_roundtrip():
    plaintext = "WEAREDISCOVEREDFLEEATONCE"
    key = 5
    ct = transposition.simple_transposition_encrypt(plaintext, key)
    pt = transposition.simple_transposition_decrypt(ct, key)
    # Some implementations change case; compare lower()
    assert pt.lower() == plaintext.lower()

def test_transposition_aliases():
    # if aliases exist as encrypt/decrypt, check them
    if hasattr(transposition, "encrypt") and hasattr(transposition, "decrypt"):
        key = 6
        text = "HELLOTRANSPOSE"
        ct = transposition.encrypt(text, key)
        assert transposition.decrypt(ct, key).lower() == text.lower()
