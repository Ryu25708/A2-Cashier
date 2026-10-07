import os

class Product:
    def __init__(self, name, category, quantity, price):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def display(self):
        return f"{self.name} | {self.category} | {self.quantity} pcs | {self.price:.2f} Baht"


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        products = file.readlines()

    print("\n--- Product List ---")

    if not products:
        print("No products found.")
        return

    for i, product in enumerate(products, 1):
        print(f"{i}. {product.strip()}")


def edit_product(filename):
    with open(filename, "r", encoding="utf-8") as file:
        products = file.readlines()

    read_file(filename)

    try:
        number = int(input("\nEnter product number to edit: ")) - 1

        if number < 0 or number >= len(products):
            print("Product not found.")
            return

        name = input("New product name: ")
        category = input("New category: ")
        quantity = int(input("New quantity: "))
        price = float(input("New price: "))

        product = Product(name, category, quantity, price)
        products[number] = product.display() + "\n"

        with open(filename, "w", encoding="utf-8") as file:
            file.writelines(products)

        print("Product updated successfully.")

    except ValueError:
        print("Invalid input.")


def delete_product(filename):
    with open(filename, "r", encoding="utf-8") as file:
        products = file.readlines()

    read_file(filename)

    try:
        number = int(input("\nEnter product number to delete: ")) - 1

        if number < 0 or number >= len(products):
            print("Product not found.")
            return

        deleted = products.pop(number)

        with open(filename, "w", encoding="utf-8") as file:
            file.writelines(products)

        print(f"Deleted: {deleted.strip()}")

    except ValueError:
        print("Invalid input.")


def create_inventory():
    filename = input("Enter inventory name: ").strip() + ".txt"

    if not os.path.exists(filename):
        open(filename, "w", encoding="utf-8").close()

    while True:
        print("\n===== CASHIER SYSTEM =====")
        print("1. Add Product")
        print("2. Read Products")
        print("3. Edit Product")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            try:
                name = input("Product name: ")
                category = input("Category: ")
                quantity = int(input("Quantity: "))
                price = float(input("Price: "))

                product = Product(name, category, quantity, price)

                with open(filename, "a", encoding="utf-8") as file:
                    file.write(product.display() + "\n")

                print("Product added.")

            except ValueError:
                print("Invalid input.")

        elif choice == "2":
            read_file(filename)

        elif choice == "3":
            edit_product(filename)

        elif choice == "4":
            delete_product(filename)

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


create_inventory()