import pickle
import random



ORDERS_FILE_PATH = "orders_data.pickle"
orders_list = []

def save_to_file(orders_list: list):
    with open(ORDERS_FILE_PATH, "wb") as file:
        pickle.dump(orders_list, file)


def load_from_file():
    with open(ORDERS_FILE_PATH, "rb") as file:
        return pickle.load(file)


def set_order(id: int, _orders_list: list):
    orders_list.append([id, _orders_list])

def display_main_menu():
    print("\nↆↆↆ MAIN MENU ↆↆↆ")
    print("1. To order")
    print("2. Add a new item to the menu")
    print("3. Delete the item from the menu")
    print("4. To show the history")
    print("5. Exit")

def get_menu():
    return [
        ["et doner", 5.0],
        ["toyuq doner", 4.5],
        ["tombik doner", 6.0],
        ["limuzin doner", 7.0],
        ["special doner", 8.0],
        ["basdirma doner", 5.5],
        ["shaurma toyuq", 4.0],
        ["shaurma et", 6.5]
    ]

def print_menu(menu_list: list):
    print("ↆↆↆ MENU ↆↆↆ\n")
    for i in range(len(menu_list)):
        print(f"{i + 1}. {menu_list[i]}")

def add_menu_item(menu_list: list):
    item_name = input("Enter the name of the new item: ")
    item_price = float(input("Enter the price of the new item: "))
    menu_list.append([item_name, item_price])
    print(f"{item_name} added to the menu.")

def delete_menu_item(menu_list: list):
    print_menu(menu_list)
    try:
        item_index = int(input(f"Select the item number to delete [1-{len(menu_list)}]: ")) - 1
        if 0 <= item_index < len(menu_list):
            deleted_item = menu_list.pop(item_index)
            print(f"{deleted_item[0]} has been deleted from the menu.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Enter a valid number.")    

def print_receipt(menu):
    items_index = []
    for id, order in orders_list:
        items_index = order.copy()

    unique_items = []

    for item in items_index:
        if item not in unique_items:
            unique_items.append(item)

    for id, order in orders_list:
        print(f"Table №{id}")
        for i in unique_items:
            print(f"{menu[i]} x{order.count(i)}")


menu = get_menu()
orders = []


while True:
    # orders_list = load_from_file()
    save_to_file(orders)
    display_main_menu()
        
    try:
        main_choice = int(input("Select an option [1-5]: "))

        if main_choice == 1:
            print_menu(menu)
            try:
                menu_choice = int(input(f"\nSelect option [1-{len(menu)}]: ")) - 1

                if not 0 <= menu_choice < len(menu):
                    print(f"The option must be between 1 and {len(menu)}.")
                    continue

                orders.append(menu_choice)

                while True:
                    question = input("Do you want to add more items to the order? [YES | NO] ").lower()
                    if question == "yes":
                        break
                    elif question == "no":
                        id = random.randint(1, 20)
                        set_order(id, orders)
                        save_to_file(orders_list)
                        break
                    else:
                        print("Wrong input! Enter again!")
                        continue

                if question == "yes":
                    continue

            except ValueError:
                print("Enter a correct number!")
                continue

            print(orders_list)
            print_receipt(menu)

        elif main_choice == 2:
            add_menu_item(menu)

        elif main_choice == 3:
            delete_menu_item(menu)

        elif main_choice == 4:
            print_receipt(menu)

        elif main_choice == 5:
            break

        else:
            print("The option must be between 1 and 5.")

    except ValueError:
        print("Enter a correct number!")
