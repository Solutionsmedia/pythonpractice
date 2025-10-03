# We can now combine what you’ve learned:
# Ask for a user’s name and age.
# Check if they’re eligible(age rules).
# Then ask for username and password.
# Check login.
# Print a custom welcome message including their name and age.
users = [
    {"username": "solutions", "password": "12345", "fullname": "Sade"},
    {"username": "alice", "password": "54321", "fullname": "Alice"},
]


def check_age():
    while True:
        name = input("Kindly Enter your name: ")
        age = int(input("Kindly Enter your age for verification: "))
        if age < 18:
            print("You are too young")
        else:
            print("You are eligile.....")
            break

    return True


def login():
    while True:
        username = input("Kindly Enter your Username: ")
        password = input("Kindly Enter your password: ")
        found = None

        for user in users:
            if user["username"] == username:
                found = user
                break

        if found is None:
            print("Username Not Found")
        elif password != found["password"]:
            print("Incorrect password, Try again")
        else:
            print("Welcome")
        break
    return {
        "user_name": found["username"],
        "full_name": found["fullname"]
    }


# Application
print("Welcome to User Verifier")
age = check_age()
if age:
    logged_in = login()
    if logged_in:
        print(f"Welcome to Your Dashboard {logged_in['user_name']}")
        print(f"Full Name is {logged_in['full_name']}")
