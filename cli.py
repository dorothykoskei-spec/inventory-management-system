import requests
from openfoodfacts import find_product_by_barcode

BASE_URL = "http://127.0.0.1:5000"


def show_menu():
    print("\n================================")
    print("   INVENTORY MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add new inventory item")
    print("2. View inventory details")
    print("3. Update item price or stock")
    print("4. Delete product")
    print("5. Find item on OpenFoodFacts")
    print("6. Exit")


def add_item():
    print("\n--- ADD NEW INVENTORY ITEM ---")

    name = input("Enter product name: ")

    if name == "":
        print("Product name cannot be empty.")
        return

    try:
        price = float(input("Enter product price: "))
        stock = int(input("Enter stock quantity: "))
    except ValueError:
        print("Invalid input. Please enter numbers for price and stock.")
        return

    data = {
        "product_name": name,
        "brands": "Local Brand",
        "ingredients_text": name,
        "price": price,
        "stock": stock
    }

    try:
        response = requests.post(
            f"{BASE_URL}/inventory",
            json=data
        )

        if response.status_code == 201:
            print("Item added successfully!")
        else:
            print("Failed to add item.")

    except requests.exceptions.RequestException:
        print("Could not connect to the Flask API.")


def view_inventory():
    print("\n--- INVENTORY DETAILS ---")

    try:
        response = requests.get(f"{BASE_URL}/inventory")

        if response.status_code != 200:
            print("Could not get inventory.")
            return

        items = response.json()

        for item in items:
            print("--------------------")
            print(f"ID: {item.get('id')}")

            product = item.get("product", {})

            print(f"Name: {product.get('product_name')}")
            print(f"Price: {item.get('price')}")
            print(f"Stock: {item.get('stock')}")

        print("--------------------")
        print(f"Total items: {len(items)}")

    except requests.exceptions.RequestException:
        print("Could not connect to the Flask API.")


def update_item():
    print("\n--- UPDATE ITEM ---")

    view_inventory()

    try:
        item_id = int(input("\nEnter the ID of the item to update: "))
    except ValueError:
        print("Please enter a valid ID number.")
        return

    print("1. Update price")
    print("2. Update stock")

    choice = input("Choose what to update: ")

    if choice == "1":

        try:
            new_price = float(input("Enter new price: "))
        except ValueError:
            print("Please enter a valid price.")
            return

        data = {"price": new_price}

    elif choice == "2":

        try:
            new_stock = int(input("Enter new stock quantity: "))
        except ValueError:
            print("Please enter a valid stock number.")
            return

        data = {"stock": new_stock}

    else:
        print("Invalid choice.")
        return

    try:
        response = requests.patch(
            f"{BASE_URL}/inventory/{item_id}",
            json=data
        )

        if response.status_code == 200:
            print("Item updated successfully!")
        elif response.status_code == 404:
            print("Product not found.")
        else:
            print("Failed to update product.")

    except requests.exceptions.RequestException:
        print("Could not connect to the Flask API.")


def delete_item():
    print("\n--- DELETE PRODUCT ---")

    view_inventory()

    try:
        item_id = int(input("\nEnter the ID of the item to delete: "))
    except ValueError:
        print("Please enter a valid ID number.")
        return

    try:
        response = requests.delete(
            f"{BASE_URL}/inventory/{item_id}"
        )

        if response.status_code == 200:
            print("Product deleted successfully!")
        elif response.status_code == 404:
            print("Product not found.")
        else:
            print("Failed to delete product.")

    except requests.exceptions.RequestException:
        print("Could not connect to the Flask API.")


def find_external_product():
    print("\n--- FIND ITEM ON OPENFOODFACTS ---")

    barcode = input("Enter product barcode: ")

    if barcode == "":
        print("Barcode cannot be empty.")
        return

    try:
        product = find_product_by_barcode(barcode)

        if product:
            print("\nProduct found!")
            print("Product:", product.get("product_name"))
            print("Brand:", product.get("brands"))
            print("Barcode:", product.get("code"))
            print("Quantity:", product.get("quantity"))
        else:
            print("Product not found.")

    except requests.exceptions.RequestException:
        print("Could not connect to OpenFoodFacts.")


def main():
    show_menu()

    while True:
        choice = input("\nChoose an option: ")

        if choice == "1":
            add_item()

        elif choice == "2":
            view_inventory()

        elif choice == "3":
            update_item()

        elif choice == "4":
            delete_item()

        elif choice == "5":
            find_external_product()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()