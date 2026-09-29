# A2 - Cashier System
# 1. Create a Product class to store item information.
# 2. Allow users to enter product details.
# 3. Save product information in a text file.

import os


class Product:
    def __init__(self, name, category, quantity, price):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def display(self):
        return f"{self.name} | {self.category} | {self.quantity} pcs | {self.price:.2f} Baht"


def create_inventory():
    filename = input("Enter inventory name: ").strip()
    path = os.path.abspath(filename + ".txt")

    print(f"\nInventory location: {path}")

    with open(path, "w", encoding="utf-8") as data:
        while True:
            print("\n--- Add New Product ---")

            name = input("Product name: ").strip()
            category = input("Product category: ").strip()

            try:
                quantity = int(input("Quantity: "))
                price = float(input("Unit price: "))

                if quantity < 0 or price < 0:
                    print("Quantity and price cannot be negative.")
                    continue

            except ValueError:
                print("Invalid input. Please try again.")
                continue

            item = Product(name, category, quantity, price)

            data.write(item.display() + "\n")
            print(f"\nProduct saved: {item.display()}")

            again = input("\nAdd another product? (Y/N): ").strip().lower()

            if again != "y":
                print("\nInventory completed.")
                print("Ready for checkout.")
                break


create_inventory()