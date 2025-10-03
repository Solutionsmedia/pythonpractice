import os
import json
import streamlit as st

file = "gibiusbank.json"


def init_db(db_file):
    if os.path.exists(db_file):
        with open(db_file, "r") as f:
            return json.load(f)
    else:
        db = []
        with open(db_file, "w") as f:
            json.dump(db, f)
        return db


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
    st.success(
        f"Dear {username}, your account has been registered successfully. Please log in.")


def login_user(users_name, passs_word):
    user_db = init_db(file)
    for user in user_db:
        if users_name == user["username"] and passs_word == user["password"]:
            st.success("Login successful")
            return user
    st.error("Wrong username or password")
    return None


# --- Streamlit App ---
st.title("🏦 Gibius Banking App")

if "loggedin" not in st.session_state:
    st.session_state.loggedin = False
if "user" not in st.session_state:
    st.session_state.user = None

menu_choice = st.sidebar.radio("Menu", ["Home", "Register", "Login", "About"])

if menu_choice == "Home":
    st.write("Welcome to Gibius Bank!")

elif menu_choice == "Register":
    st.subheader("Register New Account")
    first = st.text_input("First Name")
    last = st.text_input("Last Name")
    username = st.text_input("Username")
    email = st.text_input("Email")
    adress = st.text_area("Address")
    phone = st.text_input("Phone Number")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if len(password) < 8:
            st.error("Password must be at least 8 characters long")
        elif "@" not in email:
            st.error("Invalid email address")
        else:
            register_user(first, last, username, email,
                          adress, phone, password)

elif menu_choice == "Login":
    st.subheader("Login to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = login_user(username, password)
        if user:
            st.session_state.loggedin = True
            st.session_state.user = user

elif menu_choice == "About":
    st.info("This is a simple banking demo app built with Streamlit.")
