# Advanced Encryption Suite

A modular Python-based encryption and decryption toolkit supporting both classical and modern cryptographic algorithms. This project is designed for learning, demonstration, and extension of ciphers, hashing, and encryption modes.


🔐 Features

Classical Ciphers

| Cipher          | Encrypt | Decrypt | Brute Force | Notes                         |
| --------------- | :-----: | :-----: | :---------: | ----------------------------- |
| Caesar Cipher   |    ✅    |    ✅    |      ✅      | Integer key                   |
| Substitution    |    ✅    |    ✅    |      ➖      | Supports permutation mapping  |
| Transposition   |    ✅    |    ✅    |      ➖      | Simple & double transposition |
| Vigenère Cipher |    ✅    |    ✅    |      ➖      | Keyword-based encryption      |


Modern Symmetric Encryption (via PyCryptodome)

| Algorithm | Modes Supported | Key Type         |
| --------: | --------------- | ---------------- |
|       AES | ECB, CBC, CFB   | Default/test key |
|       DES | ECB, CBC, CFB   | Default/test key |
|      3DES | ECB, CBC, CFB   | Default/test key |

Hashing & Examples

Simple SHA-256 hashing

SHA collision/statistical testing (optional plotting)

advanced-encryption-suite/
│
├── src/
│   ├── main.py               # Main entry point (menu system)
│   ├── ciphers/
│   │   ├── caesar.py
│   │   ├── substitution.py
│   │   ├── transposition.py
│   │   └── vigenere.py
│   ├── symmetric/
│   │   └── aes_des.py
│   ├── modes/
│   │   └── modes.py
│   ├── hashing/
│   │   ├── sha_simple.py
│   │   └── sha_stats.py
│   └── utils/
│       └── helpers.py
│
├── tests/
│   └── 
├── requirements.txt
└── README.md

🛠️ Planned Improvements

Add GUI interface

Add RSA / public key cryptography

Add file encryption support

Improve test coverage

Implement brute-force solver for Substitution & Transposition

🤝 Contributing

Pull requests and new feature ideas are encouraged! Please open an issue to discuss any major changes beforehand.

📜 License

This project is for educational and demonstration purposes. You may use or modify freely with attribution.

✅ Status

🚀 Currently under development. Core encryption modules and CLI menu operational