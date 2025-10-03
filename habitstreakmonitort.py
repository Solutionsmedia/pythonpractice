import json
import os
from datetime import date

DATA_FILE = "habits.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return {"last_date": None, "habits": {}}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def show_habits(data):
    today = str(date.today())
    print(f"\n{today}")
    print("Habits:")
    for habit, info in data["habits"].items():
        status = "[x]" if info["done_today"] else "[ ]"
        print(f"{status} {habit} (streak: {info['streak']})")


def add_habit(data, habit_name):
    if habit_name in data["habits"]:
        print(f"Habit '{habit_name}' already exists.")
    else:
        data["habits"][habit_name] = {"streak": 0, "done_today": False}
        print(f"Added habit: {habit_name}")


def mark_done(data, habit_name):
    if habit_name not in data["habits"]:
        print(f"No such habit: {habit_name}")
        return
    if data["habits"][habit_name]["done_today"]:
        print(f"Habit '{habit_name}' already marked as done today.")
        return
    data["habits"][habit_name]["done_today"] = True
    data["habits"][habit_name]["streak"] += 1
    print(f"Marked '{habit_name}' as done!")


def reset_day_if_needed(data):
    today = str(date.today())
    if data["last_date"] != today:
        # If a new day started, reset done_today flags
        for habit, info in data["habits"].items():
            if not info["done_today"]:
                info["streak"] = 0  # streak broken if not done yesterday
            info["done_today"] = False
        data["last_date"] = today


def main():
    data = load_data()
    reset_day_if_needed(data)

    while True:
        show_habits(data)
        command = input("\nType a command (add/done/exit): ").strip().lower()
        if command == "exit":
            save_data(data)
            print("Goodbye!")
            break
        elif command.startswith("add "):
            habit_name = command[4:].strip()
            add_habit(data, habit_name)
        elif command.startswith("done "):
            habit_name = command[5:].strip()
            mark_done(data, habit_name)
        else:
            print("Unknown command. Use 'add <habit>', 'done <habit>', or 'exit'.")


if __name__ == "__main__":
    main()
