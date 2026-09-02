# 🔐 UGAEGQfb

**UGAEGQfb** is a local command-line text encryption tool written in Python.

The project was created as an educational cryptography and Python programming project. It demonstrates how text can be transformed using a **Caesar cipher**, how encryption/decryption functions work, how keys are generated, and how a Python CLI application can be packaged into a standalone Windows executable.

> ⚠️ **Security notice:** UGAEGQfb is an educational project. The Caesar cipher is cryptographically insecure and must **not** be used to protect real passwords, private keys, sensitive files, or confidential information.

---

## 📌 Project overview

UGAEGQfb is designed to run **locally on the user's computer**.

The application does not require:

* an internet connection,
* a remote server,
* an online database,
* an API,
* a cloud service.

The basic workflow is:

```text
User
 │
 ├── 1. Encrypt
 │      │
 │      ├── Enter plaintext
 │      ├── Generate encryption key
 │      ├── Apply Caesar cipher
 │      └── Display ciphertext + key
 │
 ├── 2. Decrypt
 │      │
 │      ├── Enter ciphertext
 │      ├── Enter key
 │      ├── Reverse Caesar transformation
 │      └── Display plaintext
 │
 └── 3. Exit
```

The project is intentionally simple so that the source code can be easily studied and modified.

---

# ✨ Features

* 🔐 Local text encryption
* 🔓 Text decryption
* 🔑 Random key generation
* 🔄 Reversible encryption
* 🖥️ Command-line interface
* 🐍 Written entirely in Python
* 📦 Can be compiled into a standalone `.exe`
* 🌐 No network communication
* 💾 No external database required
* 📚 Simple source code suitable for learning Python

---

# 🧠 How the encryption works

UGAEGQfb currently uses the **Caesar cipher**.

The Caesar cipher shifts every letter in the alphabet by a specified number of positions.

For example, with a key of `3`:

```text
A → D
B → E
C → F
D → G
...
X → A
Y → B
Z → C
```

The same principle works in the opposite direction during decryption.

### Example

Plaintext:

```text
Hello
```

Key:

```text
3
```

Encrypted text:

```text
Khoor
```

Decrypting `Khoor` with key `3` produces:

```text
Hello
```

---

# 🔢 Mathematical model

For a lowercase letter, the encryption operation can be represented as:

```text
E(x) = (x + k) mod 26
```

Where:

* `x` = numerical representation of the character
* `k` = encryption key
* `26` = number of letters in the English alphabet

Decryption uses:

```text
D(x) = (x - k) mod 26
```

This allows the encryption and decryption operations to be reversible.

---

# 🏗️ Project structure

Current project structure:

```text
UGAEGQfb.py/
│
├── UGAEGQfb.py       # Main Python application
├── UGAEGQfb.exe      # Compiled Windows executable
├── README.md         # Project documentation
└── LICENSE           # Project license
```

The main application is currently contained in a single Python file.

This is intentional for the early development stage of the project.

As the project grows, the code can be separated into modules.

For example:

```text
UGAEGQfb/
│
├── src/
│   ├── main.py
│   ├── cipher.py
│   ├── storage.py
│   └── utils.py
│
├── tests/
│   ├── test_cipher.py
│   └── test_storage.py
│
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Core functions

The project currently uses two main functions.

## `szyfruj()`

Responsible for encrypting text.

Conceptually:

```python
szyfruj(tekst, klucz)
```

Parameters:

| Parameter | Description                   |
| --------- | ----------------------------- |
| `tekst`   | Text that should be encrypted |
| `klucz`   | Caesar cipher shift           |

The function returns the encrypted text.

---

## `odszyfruj()`

Responsible for decrypting text.

Conceptually:

```python
odszyfruj(tekst, klucz)
```

Instead of implementing another encryption algorithm, decryption calls the encryption function with the negative key.

Conceptually:

```python
return szyfruj(tekst, -klucz)
```

This is possible because Caesar encryption is mathematically reversible.

---

# 🔑 Key generation

When encrypting text, the application generates a random key:

```python
klucz = random.randint(1, 25)
```

This means the key can be any integer from:

```text
1 → 25
```

The generated key is displayed to the user after encryption.

Example:

```text
Zaszyfrowano: Itcbi
Klucz: 8
```

The key is required to decrypt the ciphertext correctly.

If the ciphertext is:

```text
Itcbi
```

and the key is:

```text
8
```

the original text can be recovered.

---

# 🖥️ Command-line interface

The application starts with a simple text menu:

```text
1. Szyfruj
2. Odszyfruj
3. Wyjdź
```

The program uses a continuous loop so that the user can perform multiple operations without restarting the application.

Conceptually:

```text
START
  │
  ▼
Show menu
  │
  ├── 1 → Encrypt
  │
  ├── 2 → Decrypt
  │
  └── 3 → Exit
          │
          ▼
         END
```

---

# 🔤 Character handling

The encryption algorithm handles:

* uppercase letters,
* lowercase letters,
* spaces,
* numbers,
* punctuation,
* special characters.

Only alphabetic characters are shifted.

For example:

```text
Hello, World! 123
```

The letters can change, while:

```text
, ! 123
```

remain unchanged.

This is implemented using Python's:

```python
ord()
```

and:

```python
chr()
```

functions.

---

# 🐍 Python concepts demonstrated

This project demonstrates several important Python concepts.

### Variables

```python
tekst = input(...)
klucz = random.randint(...)
```

### Functions

```python
def szyfruj(tekst, klucz):
    ...
```

### Function arguments

```python
szyfruj(tekst, klucz)
```

### Return values

```python
return ...
```

### Loops

```python
while True:
    ...
```

### Conditional statements

```python
if wybor == "1":
    ...
elif wybor == "2":
    ...
else:
    ...
```

### User input

```python
input(...)
```

### String processing

```python
''.join(...)
```

### Random number generation

```python
random.randint(...)
```

### ASCII/Unicode conversion

```python
ord()
chr()
```

### f-strings

```python
print(f"Klucz: {klucz}")
```

These concepts form the foundation for more advanced Python applications.

---

# 📦 Running from source

## Requirements

Python 3.x is required.

Check your Python installation:

```bash
python --version
```

or:

```bash
py --version
```

---

## Clone the repository

```bash
git clone https://github.com/TechKarol/UGAEGQfb.py.git
```

Enter the project directory:

```bash
cd UGAEGQfb.py
```

Run the application:

```bash
python UGAEGQfb.py
```

On Windows, you can also use:

```bash
py UGAEGQfb.py
```

---

# 🪟 Windows executable

The project can be packaged using **PyInstaller**.

Install PyInstaller:

```bash
pip install pyinstaller
```

If the `pyinstaller` command is not available directly, use:

```bash
py -m PyInstaller --version
```

Build the executable:

```bash
py -m PyInstaller --onefile UGAEGQfb.py
```

The executable will be created in:

```text
dist/
└── UGAEGQfb.exe
```

Because the application uses `input()` and `print()`, it is intentionally built as a **console application**.

Do not use:

```bash
--noconsole
```

for the current version.

---

# 🔒 Security

UGAEGQfb should **not** be considered a secure encryption application.

The Caesar cipher has an extremely small keyspace:

```text
25 possible keys
```

An attacker can simply try every possible key.

For example:

```text
Key 1
Key 2
Key 3
...
Key 25
```

This makes the cipher trivial to break.

The random key generated by:

```python
random.randint(1, 25)
```

does not make Caesar encryption cryptographically secure.

Python's `random` module is also **not intended for cryptographic key generation**.

---

# 🧪 Why use an insecure cipher?

The purpose of this project is learning.

The Caesar cipher makes it possible to understand:

```text
plaintext
    ↓
key
    ↓
transformation
    ↓
ciphertext
```

without immediately dealing with the complexity of modern cryptographic algorithms.

After understanding this implementation, the project can evolve toward stronger cryptographic primitives.

---

# 🚀 Roadmap

Possible future development:

### Phase 1 — Basic implementation

* [x] Caesar encryption
* [x] Caesar decryption
* [x] Random key generation
* [x] CLI menu
* [x] Local operation
* [x] Windows executable

### Phase 2 — Reliability

* [ ] Input validation
* [ ] Handle invalid keys
* [ ] Handle empty input
* [ ] Better error messages
* [ ] Cleaner CLI
* [ ] Improved project structure

### Phase 3 — Local storage

* [ ] Save encrypted data locally
* [ ] Load encrypted data
* [ ] Create application data directory
* [ ] JSON-based metadata
* [ ] Separate storage module

### Phase 4 — Testing

* [ ] Unit tests
* [ ] Encryption/decryption tests
* [ ] Edge-case tests
* [ ] Automated testing

Example:

```text
encrypt(text, key)
        ↓
ciphertext
        ↓
decrypt(ciphertext, key)
        ↓
original text
```

The final result should always satisfy:

```text
decrypt(encrypt(text, key), key) == text
```

for supported input.

### Phase 5 — Cryptography

Potential future versions could replace the educational Caesar cipher with a modern cryptographic construction.

Possible areas to study:

* authenticated encryption,
* key derivation,
* password-based encryption,
* cryptographically secure random generation,
* nonce/IV handling,
* integrity verification.

The cryptographic design should be based on established libraries and standards rather than implementing a new cipher from scratch.

---

# 🧩 Development philosophy

UGAEGQfb is primarily a **learning project**.

The goal is not to create a production-grade encryption standard, but to learn how software is designed and developed.

The project provides practical experience with:

```text
Python
 │
 ├── Functions
 ├── Algorithms
 ├── Loops
 ├── Input/output
 ├── String manipulation
 ├── Randomness
 ├── File handling
 ├── Error handling
 ├── Testing
 ├── Git
 ├── GitHub
 └── Application packaging
```

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you want to modify the project:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test the application.
5. Commit your changes.
6. Open a pull request.

Example:

```bash
git checkout -b feature/improved-cli
```

Then:

```bash
git add .
git commit -m "Improve CLI handling"
git push origin feature/improved-cli
```

---

# 🐛 Issues

If you find a bug or have an idea for a feature, create an issue in the GitHub repository.

Useful bug reports should contain:

* what happened,
* what you expected,
* how to reproduce the problem,
* Python version,
* operating system,
* relevant error message.

---

# 📚 Educational purpose

This project is intended for:

* learning Python,
* learning basic cryptography concepts,
* experimenting with algorithms,
* learning Git and GitHub,
* learning software development practices,
* understanding how Python applications can be packaged.

It should not be used to protect sensitive or confidential information.

---

# ⚠️ Disclaimer

UGAEGQfb is provided for educational purposes.

The current encryption algorithm does **not provide real-world cryptographic security**.

Do not use this software to protect:

* passwords,
* API keys,
* private keys,
* financial information,
* personal confidential data,
* production secrets,
* sensitive documents.

For real security applications, use well-established cryptographic libraries and algorithms that have been publicly reviewed and are appropriate for the intended threat model.

---

# 📄 License

This project is open source.

See the `LICENSE` file for the terms under which the project is distributed.

---

# 👨‍💻 Author

**TechKarol**

GitHub:

https://github.com/TechKarol

---

# ⭐ Project status

**Status:** 🧪 Educational / Active Development

UGAEGQfb is an evolving project focused on learning Python, software engineering, and cryptography.

The architecture may change significantly as new functionality is added.

---

## 🔐 UGAEGQfb

> **Learn Python. Understand cryptography. Build software.**
