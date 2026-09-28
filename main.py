import json
import random
import string

MENU = """
1. Add password
2. Search password
3. View all passwords
4. Delete password
5. Generate password
6. Exit
"""
characters = string.ascii_letters + string.digits + string.punctuation

def load_passwords():
    with open("passwords.json") as file:
        result = json.load(file)
        return result

def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

def generate_password():
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    number = random.choice(string.digits)
    special = random.choice(string.punctuation)

    password = [lower, upper, number, special]

    for _ in range(4):
        password.append(random.choice(characters))

    random.shuffle(password)
    return "".join(password)

def add_password(passwords):
    web = input("please enter website url: ")
    user_name = input("please enter user name: ")

    question = input("Do you want to generate a password? (y/n): ")

    if question.lower() == "y":
        password = generate_password()
        print(f"Generated password: {password}")
    else:
        password = input("please enter password: ")

    info = {
        "website": web,
        "username": user_name,
        "password": password
    }

    passwords.append(info)
    save_passwords(passwords)

def search_password(passwords):
    user_search = input("Please enter site for search: ")
    matching_passwords = []

    for password in passwords:
        if user_search in password["website"]:
            matching_passwords.append(password)

    if not matching_passwords:
        print("No passwords found.")

    return matching_passwords

def view_all_passwords(passwords):
    passwords_list = list(enumerate(passwords, start=1))
    if not passwords_list:
        print("No passwords saved.")
    else:
        for password in passwords_list:
            print(f"{password[0]} _ {password[1]['website']}\n Username: {password[1]['username']}\n password: *******")

def delete_password(passwords):
    search_result = search_password(passwords)
    view_all_passwords(search_result)

    if not search_result:
        print("nothing for show")
        return
    try:
        user_choice = int(input("please enter number for delete: "))
    except ValueError:
        print("please just enter number in you show")
        return

    if user_choice > len(search_result) or user_choice <= 0:
        print("please enter valid number!!!")
        return
    
    selected = search_result[user_choice - 1]
    passwords.remove(selected)

    save_passwords(passwords)

passwords = load_passwords()
print("===== Password Manager =====")
print(MENU)

while True:
    try:
        user_choice = int(input("Choose an option: "))
    except ValueError:
        print("enter valid number!!!")
        continue
    if user_choice == 1: 
        add_password(passwords)
    elif user_choice == 2:
        search_password(passwords)
    elif user_choice == 3:
        view_all_passwords(passwords)
    elif user_choice == 4:
        delete_password(passwords)
    elif user_choice == 5:
        print(generate_password())
    elif user_choice == 6:
        break
    else:
        print("please enter valid choice")