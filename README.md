# 🔐 Password Manager CLI

A simple command-line password manager built with Python.

The application allows users to save, search, view, delete, and generate passwords. Password data is stored in a JSON file so it remains available after the program is closed.

## ✨ Features

- Add new passwords
- Search passwords by website
- View all saved passwords
- Hide passwords when displaying saved accounts
- Delete saved passwords
- Generate random passwords
- Generate passwords with:
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special characters
- Save password data to a JSON file
- Load saved passwords when the program starts
- Input validation
- Handles invalid menu and delete inputs without crashing

## 🧠 What I Learned

While building this project, I practiced:

- Functions and function responsibilities
- Lists and dictionaries
- `for` and `while` loops
- Conditional statements
- `try / except`
- Input validation
- JSON file handling
- `json.load()`
- `json.dump()`
- Reading and writing files
- Searching through dictionaries
- Removing items from lists
- The `random` module
- The `string` module
- Generating random passwords
- Working with persistent data
- Breaking a larger problem into smaller functions

## 📁 Project Structure

    password_manager/
    │
    ├── main.py
    ├── passwords.json
    └── README.md

## ▶️ How to Run

Make sure Python is installed on your computer.

Clone the repository:

    git clone YOUR_REPOSITORY_URL

Go into the project directory:

    cd password_manager

Run the application:

    python main.py

## ⚠️ Note

This project is built for learning purposes.

Passwords are stored as plain text inside a JSON file, so this application should **not** be used to store real passwords or sensitive credentials.

## 🛠️ Technologies

- Python 3
- JSON
- Git
- GitHub
