# Initialize empty shopping list
import json
shopping_db = "shopping_db.json"


def load_db(file):
    try:
        with open(file, "r") as shopfile:
            return json.load(shopfile)
    except FileNotFoundError:
        print("Network Error")


def save_db(data):
    try:
        with open(shopping_db, "w") as shopdb:
            json.dump(data, shopping_db, indent=4)
    except Exception as e:
        print("Error", e)


shopping_list = load_db(shopping_db)


print("Welcome to your Shopping List Manager!")

while True:
    print("\nOptions:")
    print("1. Add an item")
    print("2. View your list")
    print("3. To change the quantity of an item")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1/2/3/4): "))

    except ValueError:
        print("Invalid Input, only (1/2/3) ")
        continue

    if choice == 1:
        # 1. Ask for item name
        item_name = input("Enter the item name: ")
        found = False
        for item in shopping_list:
            if item_name.lower() == item["item"].lower():

                found = True
                break
        if found == False:
            # 2. Ask for quantity
            try:
                quantity = int(input("Enter the quantity: "))

            except ValueError:
                print("Invalid quantity! Please enter a number.")
                continue  # go back to the top of the loop
            shopping_list.append(
                {"item": item_name, "Item_quantity": quantity})
            try:
                with open(shopping_db, "w") as shopdb:
                    json.dump(shopping_list, shopdb, indent=4)
            except Exception as e:
                print("Error", e)
                continue
            print(f"{item_name} Just Added")
        else:
            print(f" {item_name} already exists")

    elif choice == 2:
        print("Here are Your shopping list:")
        for index,  item in enumerate(shopping_list, start=1):
            print(f" {index}. {item['item']} - {item['Item_quantity']}")

    elif choice == 3:
        change = input("Kindly Enter item you want to change quantity for")
        found = False
        for item in shopping_list:
            pre = item["Item_quantity"]
            if item["item"] == change:
                found = True
            if found:
                try:

                    new_quant = int(
                        input(f"The Currentn Quantity is {pre}, Kindly enter the new quantity."))
                except ValueError:
                    print("Kindly Enter your quantity in figures")
                    continue
                item["Item_quantity"] == new_quant
                save_db(shopping_list)
                print(f"{pre} has been changed to {item} successfully")
                continue
            else:
                print(f"{change} doesent exist in your cart")

    elif choice == 4:
        print("Goodbye!")
        break  # exit the program

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
