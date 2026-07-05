# CipherLock

**CipherLock** is a Python-based encryption and decryption application built to demonstrate the fundamentals of classical cryptography using the **Vigenère Cipher**.

Designed as a beginner-friendly cybersecurity project, CipherLock allows users to encrypt plaintext into ciphertext and decrypt it back using a shared secret key. The project focuses on helping learners understand encryption concepts, logic building, and secure programming practices.

---

## Features

* Encrypt text using the Vigenère Cipher
* Decrypt encrypted text using the same secret key
* Interactive command-line interface
* Secret key validation
* Preserves spaces and punctuation
* Cross-platform support
* Lightweight with no external dependencies
* Clean, well-documented Python code

---

# 🖼 Project Preview


## Home Screen

<p align="left">
<img src="Cipherlock Image/screenshotshome.png.png" width="900">
</p>

---

## Encryption Demo

<p align="left">
<img src="Cipherlock Image/screenshotsencryption.png.png" width="900">
</p>


---

## Decryption Demo

<p align="left">
<img src="Cipherlock Image/screenshotsencryption.png.png" width="900">
</p>

---

## Encryption and Decryption Demo

<p align="left">
<img src="Cipherlock Image/screenshotsencryption&decrypyion.png.png" width="900">
</p>

---

## About Page

<p align="left">
<img src="Cipherlock Image/screenshotsabout.png.png" width="900">
</p>
---

## Project Structure

```text
CipherLock/
│
├── cipherlock.py
│
├── screenshots/
│   ├── home.png
│   ├── encryption.png
│   ├── decryption.png
│   ├── encryption&decrypyion.png
│   └── about.png
│
├── LICENSE
└── README.md


```
Installation

Clone the repository
```bash
git clone https://github.com/Niyidegreat/cipherLock.git
```

Move into the project directory

```bash
cd cipherlock
```

Run the application

```bash
python cipherlock.py
```

---

# 🔐 How CipherLock Works

CipherLock uses the **Vigenère Cipher**, a classical symmetric encryption algorithm.

Unlike the Caesar Cipher, which shifts every character by the same amount, the Vigenère Cipher uses a keyword to produce multiple shifting values, making it significantly more secure than a fixed-shift cipher.

## Example Workflow

1. Launch the application.
2. Choose **Encrypt Text**.
3. Enter the message you want to encrypt.
4. Provide a secret key.
5. View the encrypted message.
6. Choose **Decrypt Text**.
7. Enter the encrypted message and the same secret key.
8. Recover the original message.

Example Result

| Plain Text  | HELLO WORLD |
| ----------- | ----------- |
| Secret Key  | SECURITY    |
| Cipher Text | ZINCSPGVNU  |

The same secret key is required to decrypt the encrypted message.

---

## Concepts Demonstrated

* Classical Cryptography
* Symmetric Encryption
* Vigenère Cipher
* Data Protection Basics
* Modular Arithmetic
* String Manipulation
* Input Validation
* Python Programming
* Secure Coding Principles

---

## Educational Purpose

CipherLock was created for learning and demonstration purposes.

While the Vigenère Cipher is historically significant, it is no longer considered secure for protecting sensitive information. Modern applications should use established cryptographic algorithms such as AES, RSA, or ChaCha20 through trusted cryptographic libraries.

---

## Developer

**Adeniyi Ojedele**

AI + Cybersecurity + Software | Building, Breaking & Securing Systems | Product & Graphic Designer

Passionate about building practical cybersecurity projects, documenting cyber, and making cybersecurity concepts simple and accessible.

---

## Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository, submit issues, or open pull requests.

---

## License

This project is licensed under the MIT License.

---

## Support

If you found this project useful, consider giving the repository a ⭐ on GitHub. Feedback and suggestions are always appreciated.
