from datetime import datetime, date, time, timedelta
import csv
import json
import os

name = "Sam"
habit_status = False
time_log = datetime.now()
search = ""


def add_habit():
    new_habit = input("enter new habit")
    if not habit_status:
        status = "undone"
    else:
        status = "done"
    time_log = datetime.now().isoformat()  # convert datetime to string
    data = []

    # If file exists, load existing JSON
    if os.path.exists("habit.json"):
        with open("habit.json", "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []  # file was empty or invalid

    # Add the new entry
    data.append({
        "name": name,
        "Book": new_habit,
        "Status": status,
        "TimeOfAppend": time_log
    })

    # Save back as a JSON array
    with open("habit.json", "w") as f:
        json.dump(data, f, indent=4)


def search_habit():
    try:
        search = input(
            "Kindly Enter the name of the book you want to search for: ").lower()
        with open("habit.json", "r") as habitdb:
            data = json.load(habitdb)
            for Book in data:
                if search.lower() in data:
                    print(
                        F" book {search} has been found what will you like to do to it? : ")
                else:
                    print(f"{search}NOT FOUND")
    except Exception as e:
        print("something is wrong,", e)


print("welcome")
add_habit()
