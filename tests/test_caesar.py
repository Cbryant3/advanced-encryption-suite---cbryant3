# tests/test_caesar.py
from src.ciphers import caesar

def test_roundtrip():
    pt = 'Hello, Unit Test!'
    key = 4
    ct = caesar.encrypt(pt, key)
    assert caesar.decrypt(ct, key) == pt

