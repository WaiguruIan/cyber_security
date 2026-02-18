#Adm No. : BSCIT-05-0096/2024
#Name : Ian Waiguru

import hashlib #I Imported the 'hashlib' module for secure password hashing
import os #I Imported the 'os' module for generating random salt used in password hashing
import re  #I Imported the 're' module for regular expressions


# Simulated Database 
# In a real application, this would be a secure database, not an in-memory dictionary.
database = {}

def register():
    # I used this to enter the username/password
    #I added a feature that checks if the username is available in the database and tell the person that it is there and to try another username
    while True:
        username = input("Enter a new username: ")

        # Check if the username already exists in the database
        if username in database:
            print(f"\n[ERROR] The username '{username}' is already taken. Please try another username.\n")
        else:
            break  # Exit the loop if the username is available

    while True:
        password = input("Enter a new password: ")

        # I used this to validate the password using a regular expression that checks for the required criteria (at least 8 characters, one uppercase letter, one lowercase letter, one number, and one special character). If the password does not meet the criteria, an error message is displayed and the user is prompted to enter a new password until a valid one is provided.
        if not re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%#*?&])[A-Za-z\d@$!#%*?&]{8,}$', password):
            print(f"[DEBUG] Password '{password}' did not match the criteria.")
            print("\n[ERROR] The Password must be at least 8 characters long, include uppercase, lowercase, a number, and a special character.\n")
            # Loop continues until a valid password is entered
        else:
            print(f"[DEBUG] Password '{password}' is valid.")
            break  # Exit the loop if the password is valid

    salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    
    database[username] = { # This Stores the salt and hash in the database
        'salt': salt,
        'hash': hashed,
        'attempts': 0,
        'locked': False
    }
    print(f"\n[SUCCESS] User '{username}' registered!\n")


def login():  # I used this to login the user
    username = input("Enter the Username: ")
    password = input("Enter the Password: ")

    if username not in database:
        print("\n[ERROR] User not found.\n")
        return

    user = database[username]  # This retrieves the user data from the database

    if user['locked']:
        print("\n[DENIED] This Account is LOCKED. Contact admin at 012972141 or adminsecurity@secure.com.\n")
        return

    # This Checks the password
    try:
        attempt_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), user['salt'], 100000)
    except Exception as e:  # Catch any exceptions that occur during hashing, such as encoding issues or other unexpected errors
        print(f"[ERROR] Hashing failed: {e}")
        return

    # This Compares the attempted hash with the stored hash
    if attempt_hash == user['hash']:
        print(f"\n[SUCCESS] Welcome {username}, you are logged in!\n")
        user['attempts'] = 0
    else:
        user['attempts'] += 1
        print("\n[ERROR] Incorrect password.")
        print(f"[WRONG] Attempt {user['attempts']}/3.")
        if user['attempts'] >= 3:
            user['locked'] = True
            print("[LOCKED] Too many failures. Account is now locked.\n")

# This is the Main program loop in the form of a menu
while True:
    print("Welcome to the Secure Login System")
    print("1. Register") 
    print("2. Login")  
    print ("3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")