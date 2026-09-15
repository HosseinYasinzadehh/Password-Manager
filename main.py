import json

def load_passwords():
    with open("passwords.json") as file:
        result = json.load(file)
        return result

def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

