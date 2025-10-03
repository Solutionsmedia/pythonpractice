import os
import json
from rich.console import Console
from rich.panel import Panel
import random
from datetime import datetime
import random
import streamlit as display
logfile = "log.js   uon"
file = "gibiusbank.json"


# print("Inititializng Database.....")
# init_db(file)
# print("Initialization complete")
# console = Console()
# console.print(Panel("Welcome to Gibius Banking App",
#              title="Gibius Bank", style="green"))
# user_need = str(input('''What would you love to do today?\n
#                      1. Login
#                      2. Register
#                      3. About the bank
#
#                      '''))


# Fucntion for Database Initialization
def init_db(db_file):
    if os.path.exists(db_file):
        with open(db_file, "r") as f:
            return json.load(f)
    else:
        db = []
        with open(db_file, "w") as f:
            json.dump(db, f)
            return db


def check_bvn(users):
    db_file = init_db(file)        # load all users from file
    for user in db_file:           # go through each user in the db
        if users["user_name"] == user["username"]:  # found matching user
            # check if this user has a BVN field (or whatever condition you need)
            if "bvn" in user:      # check if key "bvn" exists in the dictionary
                return True        # BVN found
            else:
                return False       # user found but no BVN
    return False                   # no matching user at all


def init_log(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    else:
        return None

# Function  for logged in or non logged in user


def menu(loggedin):
    if loggedin:
        while loggedin:
            try:

                user_need = int(input('''
            1. Withrwal
            2. Deposit
            3. Account Information
            4. Change Pin
            5. Change Password
            6. Transactions \n
            Kindly enter your choice here: '''))
            except ValueError:
                print("Kindly Enter a valid digit between 1 and 6")
                continue
            menu_list = [1, 2, 3, 4, 5, 6]
            if user_need in menu_list:
                return user_need
            else:
                print("Kindly Enter a valid choice between 1 and6")
                return None

    else:
        while True:
            try:
                user_need = int(input('''
            1. Register
            2. Log In
            3. Bank Information \n Kindly Enter you choice here: '''))
            except ValueError:
                print("Kindly Enter a valid digit between 1 and 3 please")
                continue
            menu_list = [1, 2, 3]
            if user_need in menu_list:
                return user_need
            else:
                print("Kindly Enter valid choice between 1 and 3")
                continue


# Function for Registration


def register_user(first_name, last_name, username, email, adress, phone_number, pass_word):
    db = init_db(file)
    new_user = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "email": email,
        "adress": adress,
        "phone_number": phone_number,
        "password": pass_word,
        "balance": 0
    }
    db.append(new_user)

    with open(file, "w") as f:
        json.dump(db, f, indent=4)
    print(f"Dear {username}, Your Account has been successfully registered, kindly log in to your account.")


def login_user(users_name, passs_word):
    while True:
        user_db = init_db(file)
        for user in user_db:
            if users_name == user["username"] and passs_word == user["password"]:

                print("Login Successfull")
                return {
                    "first_name": user["first_name"],
                    "last_name": user["last_name"],
                    "user_name": user["username"],
                    "email": user["email"],
                    "adress": user["adress"],
                    "phone_number": user["phone_number"],
                    "password": user["password"],
                    "balance": user["balance"],
                    "pin": user["pin"]
                }
        else:
            print("Wrong username or password")
            return None


def check_balance(user):
    userdb = init_db(file)
    for u in userdb:
        if user["user_name"] == u["username"]:
            return float(u["balance"])

    # user_balance = float(user["balance"])
    # print(f"N{user_balance}")


def log_transactions(user, trans_type, amount, balance, timestamp):

    if os.path.exists(logfile):
        with open(logfile, "r") as f:
            log = json.load(f)
            log.append({
                "User": user,
                "Status": trans_type,
                "Amount": amount,
                "Wallet Balance": balance,
                "Time": timestamp
            })
        with open(logfile, "w") as f:
            json.dump(log, f, indent=4)
    else:
        log = []
        log.append({
            "User": user,
            "Status": trans_type,
            "Amount": amount,
            "Wallet Balance": balance,
            "Time": timestamp
        })
        with open(logfile, "w") as f:
            json.dump(log, f, indent=4)


def dashboard(user):
    users = init_db(file)
    loggedin = True
    while loggedin:
        print(f"Hi {user["user_name"]}, Welcome to your account")
        print(f"Your balance is {check_balance(user)}")
        choice = menu(loggedin)
        if choice == 1:

            transtype = "Withrawal"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Welcome {user["user_name"]}")
            print(f"Your balance is {check_balance(user)}")
            withrawal = float(
                input("Kindly Enter the Amount you want to withrwal: "))
            if withrawal > user["balance"]:
                print("Insufficient Balance")
                continue
            else:
                new_balance = user["balance"] - withrawal
                for u in users:
                    if u["username"] == user["user_name"]:
                        u["balance"] = new_balance
                        break
                with open(file, "w") as f:
                    json.dump(users, f, indent=4)
                    log_transactions(user["user_name"], transtype,
                                     withrawal, new_balance, timestamp)
                print(
                    f"Withrawal Complete, your balance is{new_balance}")
                print("'VUM'Take Your Cash below")
                continue
        elif choice == 2:
            transtype = "Deposit"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Welcome{user["user_name"]}")
            print(f"Balance: {check_balance(user)}")
            deposit = float(
                input("Kindly Enter the ammount you want to deposit"))
            new_balance = check_balance(user)+deposit
            for u in users:
                if u["username"] == user["user_name"]:
                    u["balance"] = new_balance
                    break
            with open(file, "w") as f:
                json.dump(users, f, indent=4)
                log_transactions(user["user_name"], transtype,
                                 deposit, new_balance, timestamp)
                print(
                    f"Your account has successfully been funded, your new balance is {new_balance}")
                continue

        elif choice == 3:
            print("Welcome to your account")
            print(f'''Name: {user["first_name"]} {user["last_name"]}
    User Name: {user["user_name"]}
    Balance: {user["balance"]}
    Email: {user["email"]}
    Address: {user["adress"]}
    Phone Number: {user["phone_number"]}
    password:  {user["password"]}
    ''')
            continue
        elif choice == 4:
            print("Welcome to Account Management")
            print("Change your pin")
            password = input("Kindly Enter your Password")
            if password == user["password"]:
                print("Verification Successful")
            else:
                print("Wrong Password")
                continue
            try:

                new_pin = int(input("Kindly Enter your new pin: "))
            except ValueError:
                print("Kindly Enter a valid pin")
                continue
            for u in users:

                if u["username"] == user["user_name"]:
                    u["pin"] = new_pin
                with open(file, "w") as f:
                    json.dump(users, f, indent=4)
                print("Pin Successfully Changed")
                continue
        elif choice == 5:
            print(
                f"Welcome {user['user_name']} kindly verifiy your account with your 4 digit pin to change your password")
            pin = input("Kindly Enter your pin")
            if pin == user["pin"]:
                print("Verification Successfull")
                new_password = input("Kindly Enter your new password")
                for u in users:
                    if u["username"] == user["user_name"]:
                        u["password"] = new_password
                        print(
                            f"Dear {user["user_name"]}, Your password has been changed successfully")
                        continue
        elif choice == 6:
            print(
                f"Hi, {user["user_name"]}, Welcome to your Account History, below are your account transaction History")
            logger = init_log(logfile)
            for transaction in logger:
                if transaction["User"] == user["user_name"]:
                    transaction = {
                        "name": transaction["User"],
                        "trans_type": transaction["Status"],
                        "amount": transaction["Amount"],
                        "balance": transaction["Wallet Balance"],
                        "time": transaction["Time"]

                    }
                    print("name: ", transaction["name"], "~",
                          "Action: ", transaction["trans_type"], "~", "Amount: ", transaction["amount"], "~", "Balance: ", transaction["balance"], "~", "TIme: ", transaction["time"])


def main():
    loggedin = False
    while True:
        choice = menu(loggedin)
        if choice == 1:
            print("Thank you for choosing gibius Bank.")
            print("We would commence your registration process shortly.......")
            first_name = input("Kindly enter your first name: ")
            last_name = input("Kindly Enter your lastname: ")
            user_name = input(
                "Kindly Enter your username, You will need this to acesss your acccount: ")
            while True:
                email = input("Kindly Enter your Email: ")
                if "@" not in email:
                    print("Your Email is not correct, must include @")
                else:
                    break
            adress = input("Kindly enter your Address: ")
            phone_number = input("Kindly Enter your phone number: ")

            while True:
                password = input("Kindly Enter your password: ")

                if len(password) < 8:
                    print("Your passoword must not be less than 8 digits")
                    continue
                else:
                    register_user(first_name, last_name, user_name,
                                  email, adress, phone_number, password)
                    continue
        elif choice == 2:
            user_name = input("Kindly Enter your username: ")
            pass_word = input("Kindly enter your password: ")
            user_detail = login_user(user_name, pass_word)
            if not user_detail:
                continue
            bvn_status = check_bvn(user_detail)
            if bvn_status:
                dashboard(user_detail)
            else:

                print("Kindly Verify Your Account with your bvn")
                print("Do you have your BVN??")
                try:
                    bvn = int(
                        input("If you do, Kindly Enter your BVN here if not click 0"))
                except ValueError:
                    print("Only Digits please")
                    continue
                if bvn == 0:
                    print("Kidnly Hold on while we generate one for you please")
                    bvn = random.randint(10**10, 10**11 - 1)
                    print(bvn)
                    db = init_db(file)
                    for user in db:
                        if user["username"] == user_detail["user_name"]:
                            user["bvn"] = bvn
                            with open(file, "w") as f:
                                json.dump(db, f, indent=4)
                            print(
                                f"Your BVN has been generated successfully, your Bank Verification Number is {bvn}")
                            continue

                else:
                    if bvn.len() == 11:
                        print("Your Bvn is accepted")
                        continue
                    else:
                        print("Your BVN must be 11 digits")
                        continue


if __name__ == "__main__":
    main()
