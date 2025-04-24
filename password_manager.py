import json
from cryptography.fernet import Fernet
import getpass

def generate_key():
    return Fernet.generate_key()

def encrypt_password(password, key):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password

def save_passwords(passwords):
    with open('passwords.json', 'w') as f:
        json.dump(passwords, f)

def load_passwords():
    try:
        with open('passwords.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def main():
    key = generate_key()  # Generate a new key
    passwords = load_passwords()  # Load existing passwords

    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            account = input("Enter the account name: ")
            password = getpass.getpass ("Enter the password: ")
            encrypted_password = encrypt_password(password, key)
            passwords[account] = encrypted_password.decode()  # Store as string
            save_passwords(passwords)
            print("Password saved successfully!")

        elif choice == '2':
            account = input("Enter the account name: ")
            if account in passwords:
                encrypted_password = passwords[account].encode()
                decrypted_password = decrypt_password(encrypted_password, key)
                print(f"Password for {account}: {decrypted_password}")
            else:
                print("Account not found.")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()