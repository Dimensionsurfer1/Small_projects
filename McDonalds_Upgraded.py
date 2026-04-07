import csv
import os
from datetime import datetime

# --- Menu with prices ---
menu = {
    1: {"name": "Cheeseburger", "price": 3.99},
    2: {"name": "Fries",        "price": 1.99},
    3: {"name": "Soda",         "price": 1.49},
    4: {"name": "Ice Cream",    "price": 2.49},
    5: {"name": "Cookie",       "price": 0.99},
}

cart = []
ORDER_LOG = "order_history.csv"


def welcome():
    print("\n" + "="*40)
    print("   Welcome to McDonald's! Pa Ra Pa Pa Pa!")
    print("="*40)
    print("What can I get for you today?\n")


def display_menu():
    print("{:<5} {:<15} {}".format("No.", "Item", "Price"))
    print("-" * 30)
    for num, item in menu.items():
        print("{:<5} {:<15} ${:.2f}".format(num, item["name"], item["price"]))
    print()


def get_valid_item():
    """Keeps asking until the user enters a valid menu number."""
    while True:
        try:
            choice = int(input("Enter item number (1-5): "))
            if choice in menu:
                return choice
            else:
                print("  Invalid choice. Please pick a number between 1 and 5.")
        except ValueError:
            print("  Please enter a number, not text.")


def calculate_bill(cart):
    total = sum(item["price"] for item in cart)
    return round(total, 2)


def print_receipt(cart):
    total = calculate_bill(cart)
    print("\n" + "="*40)
    print("           YOUR RECEIPT")
    print("="*40)
    for item in cart:
        print("  {:<18} ${:.2f}".format(item["name"], item["price"]))
    print("-" * 40)
    print("  {:<18} ${:.2f}".format("TOTAL", total))
    print("="*40)
    return total


def save_order(cart, total):
    """Saves each order to a CSV file for order history."""
    file_exists = os.path.exists(ORDER_LOG)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items_str = ", ".join(item["name"] for item in cart)

    with open(ORDER_LOG, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Items Ordered", "Total (USD)"])
        writer.writerow([timestamp, items_str, f"${total:.2f}"])

    print(f"\n  Order saved to '{ORDER_LOG}'.")


def ask_yes_no(prompt):
    """Validates yes/no input so the program never crashes on bad input."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("  Please type 'yes' or 'no'.")


# --- Main Program ---
welcome()

if ask_yes_no("Are you at the counter? (yes/no): "):
    while True:
        display_menu()
        choice = get_valid_item()
        selected = menu[choice]
        cart.append(selected)
        print(f"  '{selected['name']}' added to your cart.\n")

        if not ask_yes_no("Would you like to order anything else? (yes/no): "):
            break

    total = print_receipt(cart)
    save_order(cart, total)
    print("\nThank you for visiting McDonald's! Have a great day!")
else:
    print("\nNo problem! Come back anytime. Have a great day!")
