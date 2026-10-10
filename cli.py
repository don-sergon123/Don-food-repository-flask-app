import requests

BASE_URL = "http://127.0.0.1:5000/inventory"

def view_inventory():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        items = response.json()
        print("\n--- Current Inventory ---")
        for item in items:
            print(
                f"ID: {item['id']} | Name: {item['product_name']} | Brand: {item['brands']} | Qty: {item['quantity']} | Price: {item['price']}")
    else:
        print("Failed to fetch inventory.")

def add_inventory_item():
    name = input("Enter product name: ")
    brand = input("Enter brand: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    payload = {"product_name": name, "brands": brand,
               "quantity": qty, "price": price}
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 201:
        print("Item added successfully!")
    else:
        print("Error adding item:", response.json())

def main_menu():
    while True:
        print("\n=== Food Inventory CLI ===")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_inventory()
        elif choice == "2":
            add_inventory_item()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
