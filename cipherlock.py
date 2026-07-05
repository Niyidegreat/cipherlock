"""
===============================================================
 Project Name : cipherlock
 Description  : Text Encryption and Decryption Tool
 Algorithm    : Vigenère Cipher
 Language     : Python 3

 Developed By : Adeniyi Ojedele
 Version      : 1.0
===============================================================
"""

import string
import os
import sys

# ==========================
# CONFIGURATION
# ==========================

APP_NAME = "cipherlock"
VERSION = "1.0"
OWNER = "Adeniyi Ojedele (Niyi De Great)"

ALPHABET = string.ascii_uppercase


# ==========================
# UTILITY FUNCTIONS
# ==========================

def clear():
    """Clear terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress ENTER to continue...")


def line():
    print("=" * 65)


def banner():
    clear()
    line()
    print(f"{APP_NAME:^65}")
    print("Simple Encryption & Decryption Tool".center(65))
    line()
    print(f"Developer : {OWNER}")
    print(f"Version   : {VERSION}")
    line()


# ==========================
# KEY FUNCTIONS
# ==========================

def clean_key(key):
    """
    Removes all non-alphabet characters.
    """

    key = "".join(c for c in key.upper() if c.isalpha())

    if not key:
        raise ValueError("Key must contain alphabetic characters only.")

    return key


def generate_key(text, key):
    """
    Repeats the key to match the message length.
    Spaces and punctuation are preserved.
    """

    key = clean_key(key)

    generated = ""
    index = 0

    for char in text:

        if char.upper() in ALPHABET:
            generated += key[index % len(key)]
            index += 1

        else:
            generated += char

    return generated


# ==========================
# ENCRYPTION
# ==========================

def encrypt(text, key):

    text = text.upper()

    key = generate_key(text, key)

    encrypted = ""

    for t, k in zip(text, key):

        if t in ALPHABET:

            p = ALPHABET.index(t)
            s = ALPHABET.index(k)

            encrypted += ALPHABET[(p + s) % 26]

        else:
            encrypted += t

    return encrypted


# ==========================
# DECRYPTION
# ==========================

def decrypt(ciphertext, key):

    ciphertext = ciphertext.upper()

    key = generate_key(ciphertext, key)

    decrypted = ""

    for c, k in zip(ciphertext, key):

        if c in ALPHABET:

            p = ALPHABET.index(c)
            s = ALPHABET.index(k)

            decrypted += ALPHABET[(p - s) % 26]

        else:
            decrypted += c

    return decrypted


# ==========================
# OPERATIONS
# ==========================

def encrypt_text():

    banner()

    print("TEXT ENCRYPTION\n")

    text = input("Enter your message : ")

    key = input("Enter secret key   : ")

    try:

        encrypted = encrypt(text, key)

        line()
        print("Encrypted Text")
        line()
        print(encrypted)

    except Exception as e:
        print("\nError:", e)

    pause()


def decrypt_text():

    banner()

    print("TEXT DECRYPTION\n")

    text = input("Enter encrypted text : ")

    key = input("Enter secret key     : ")

    try:

        decrypted = decrypt(text, key)

        line()
        print("Decrypted Text")
        line()
        print(decrypted)

    except Exception as e:
        print("\nError:", e)

    pause()


def encrypt_decrypt():

    banner()

    print("ENCRYPT & DECRYPT DEMO\n")

    text = input("Enter message : ")

    key = input("Enter key     : ")

    try:

        encrypted = encrypt(text, key)

        decrypted = decrypt(encrypted, key)

        line()
        print("Original Message")
        line()
        print(text)

        line()
        print("Encrypted Message")
        line()
        print(encrypted)

        line()
        print("Decrypted Message")
        line()
        print(decrypted)

    except Exception as e:
        print("\nError:", e)

    pause()


def about():

    banner()

    print("ABOUT\n")

    print(f"Application : {APP_NAME}")
    print(f"Version     : {VERSION}")
    print(f"Developer   : {OWNER}")

    print("\nPurpose")
    print("-" * 40)

    print(
        "CipherGuard demonstrates the implementation of a "
        "basic symmetric encryption algorithm (Vigenère Cipher). "
        "It enables users to securely encrypt and decrypt text "
        "using a shared secret key."
    )

    print("\nConcepts Demonstrated")
    print("-" * 40)

    print("• Cryptography Fundamentals")
    print("• Encryption & Decryption")
    print("• Symmetric Key Encryption")
    print("• Modular Arithmetic")
    print("• Secure Data Representation")
    print("• Python Programming")

    pause()


# ==========================
# MENU
# ==========================

def menu():

    while True:

        banner()

        print("MAIN MENU\n")

        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Encrypt & Decrypt Demo")
        print("4. About")
        print("5. Exit")

        choice = input("\nSelect Option: ").strip()

        if choice == "1":
            encrypt_text()

        elif choice == "2":
            decrypt_text()

        elif choice == "3":
            encrypt_decrypt()

        elif choice == "4":
            about()

        elif choice == "5":

            banner()

            print("Thank you for using CipherGuard.")
            print("Developed by Adeniyi Ojedele.")

            sys.exit()

        else:

            print("\nInvalid option.")

            pause()


# ==========================
# MAIN PROGRAM
# ==========================

if __name__ == "__main__":
    menu()