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

def search_password(passwords):
    matching = False
    user_search = input("Please enter site for search: ")
    for password in passwords:
        if user_search in password["website"]:
            matching = True
            print(password)
    if  not matching:
        print("No passwords found.")

passwords = load_passwords()
add_password(passwords)
search_password(passwords)