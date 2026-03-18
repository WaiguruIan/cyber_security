Secure Login System (Python)
A robust command-line interface (CLI) application demonstrating secure user registration and authentication practices. This system focuses on protecting user credentials using modern cryptographic standards.

Features
User Registration: Validates unique usernames to prevent duplicates.

Password Complexity: Implements Regex (Regular Expressions) to enforce strong password policies:

Minimum 8 characters.

At least one uppercase and one lowercase letter.

At least one numerical digit.

At least one special character (e.g., @, $, !).

Account Locking: Security measure that automatically locks an account after 3 failed login attempts to prevent brute-force attacks.

Input Validation: Robust handling of user inputs and error messaging.

Security Implementation
This project prioritizes data security by avoiding the storage of plain-text passwords.

1. Hashing and Salting
The system uses the hashlib and os modules to process passwords:

Salting: A unique, random 16-byte salt is generated for every user using os.urandom(). This ensures that two users with the same password will have different hashes.

PBKDF2-HMAC: The system utilizes the PBKDF2 (Password-Based Key Derivation Function 2) with the SHA-256 algorithm and 100,000 iterations. This makes the hash computationally expensive to crack.

2. Simulated Database
For demonstration purposes, user data is stored in an in-memory dictionary. In a production environment, this would be replaced by a persistent SQL or NoSQL database.

Prerequisites
Python 3.x

Standard libraries used: hashlib, os, re (No external installations required).

How to Run
Clone or Download the script to your local machine.

Open your terminal or command prompt.

Navigate to the directory containing the file.

Run the script using:

Bash
python your_script_name.py
Usage
Register: Select option 1 to create a new account. Follow the prompts to meet the password requirements.

Login: Select option 2. If you enter the wrong password 3 times, your account will be marked as LOCKED.

Exit: Select option 3 to close the application.
