import json

def load_passwords():
    with open("passwords.json") as file:
        result = json.load(file)
        return result

def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

def add_password(passwords):
    web = input("please enter website url: ")
    user_name = input("please enter user name: ")
    password = input("please enter password: ")

    info = {
    "website": web,
    "username": user_name,
    "password": password
    }

    passwords.append(info)
    save_passwords(passwords)

passwords = load_passwords()
add_password(passwords)