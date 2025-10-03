import json
import os
from datetime import datetime, date, time
time_now = datetime.now()
data = []
print(time_now)
full_name = []


def register():

    username = input("KIndly Enter Your Username")
    password = input("Kindly Enter your password")
    full_name = input("Kindly Enter Your full name")

    data.append({
        "name": full_name,
        "username": username,
        "password": password,
    })

    if os.path.exists("habit.json"):
        with open("habit.json", "a") as habitdb:
            json.dump(data, habitdb, indent=4)
            print(f"Hi {full_name}, Registration Successful!")
    else:
        print("Registration Failed due to network error Contact the admin")


def login():
    user_name = input("KIndly Enter your username")
    pass_word = input("kindly Enter your password")
    if os.path.exists("habit.json"):
        with open("habit.json", "a") as habitdb:
            data = json.load(habitdb)
            if user_name in data and pass_word in data:
                print("Login Successfull")


login()
