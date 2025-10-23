# tests/test_hashing.py
import importlib
import hashlib
from src.hashing import sha_simple

def test_sha_simple_runs(capsys):
    # sha_simple.run() should print a SHA-256 for the hardcoded name
    # We don't assert exact hex here: just that a 64-character hex string is printed.
    sha_simple.run()
    captured = capsys.readouterr().out
    # find 64 hex chars in output
    import re
    match = re.search(r"[0-9a-fA-F]{64}", captured)
    assert match is not None
