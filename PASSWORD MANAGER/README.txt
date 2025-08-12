Password Manager

Description:
A Python program to securely store and retrieve passwords using encryption.
It uses the cryptography library's Fernet encryption to protect stored passwords.

Features:
- Add new passwords (encrypted before storage)
- View existing passwords (decrypted when displayed)
- Persistent encryption key stored in a file (key.key)
- Passwords stored in passwords.txt

How It Works:
1. The program checks for the existence of "key.key"
   - If not found, it generates one and saves it.
   - This key is used for both encryption and decryption.
2. Adding passwords:
   - User inputs username and password.
   - Password is encrypted and stored in "passwords.txt".
3. Viewing passwords:
   - Program reads stored data and decrypts passwords before displaying.

Requirements:
- Python 3.x
- cryptography library (install using: pip install cryptography)

Important:
- Do not delete or modify the "key.key" file after passwords are stored.
  Without it, you cannot decrypt stored passwords.

How to Run:
1. Save the script as password_manager.py
2. Open terminal/command prompt in the script's folder
3. Run: python password_manager.py
4. Follow the prompts to add or view passwords.

Example:
Would you like to add a new password or view existing ones (view, add), press q to quit? add
User: john_doe
Password: mysecret123

Would you like to add a new password or view existing ones (view, add), press q to quit? view
User: john_doe | Password: mysecret123
