from cryptography.fernet import Fernet
import os


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(
            key
        )  # after generating key once, i commented it, beacuse every time i run the program, it generates new and different key which can lead to error, so in order to avoid any type of error for future use of program and to access stored user name and passwords i have to comment it


def load_key():
    with open("key.key", "rb") as f:
        key = f.readline()
    return key


if not os.path.exists("key.key"):
    write_key()
key = load_key()

fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print(f"User: {user} | Password : {fer.decrypt(pwd.encode()).decode()}")


def add():
    user = input("User : ")
    pwd = input("Password : ")
    with open("passwords.txt", "a") as file:
        file.write(user + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
