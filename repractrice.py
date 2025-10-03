import os
import json

user_db = "users.json"


def register():
    Full_name = input("Kindly Enter your full name: ")
    user_name = input("Kindly Enter Your Username (used for login): ")
    pass_word = input("Kindly Enter your Password: ")

    db_data = {
        "fullname": Full_name,
        "user_name": user_name,
        "password": pass_word
    }

    if os.path.exists(user_db):
        with open(user_db, "r") as file:
            users = json.load(file)
    else:
        users = []  # start with empty list if no file yet

    users.append(db_data)

    with open(user_db, "w") as file:
        json.dump(users, file, indent=4)
    print("Registration successful!")


def login():
    while True:
        log_name = input("Kindly Enter Your Username: ")
        log_pass = input("Kindly Enter your Password: ")

        with open(user_db, "r") as logdb:
            log_data = json.load(logdb)

        for user in log_data:
            if log_name == user["user_name"] and log_pass == user["password"]:
                return {
                    "fullname": user["fullname"],
                    "username": user["user_name"]
                }

        # if loop finishes without return
        print("You are not registered. Try again.")


def show_dash(user_dash):
    print(f"Welcome to your dashboard {user_dash['fullname']}")


loggedin_user = login()
if loggedin_user:
    print("Welcome")
    print("welcome", loggedin_user["fullname"])
    show_dash(loggedin_user)
