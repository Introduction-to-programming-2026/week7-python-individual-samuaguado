# Project 5 — Shopping Cart
# Author: Samuel Aguado

cart = {}

print("Welcome to the Shopping Cart!")
print("Type 'done' to finish.\n")

while True:
    item = input("Enter item name: ").strip()

    if item.lower() == "done":
        break

    if item == "":
        print("Item name cannot be empty.")
        continue

    try:
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        continue

    if item in cart:
        cart[item]["quantity"] += quantity
    else:
        cart[item] = {"price": price, "quantity": quantity}

print("\n=== Shopping Cart Summary ===")

total = 0

for item, data in cart.items():
    subtotal = data["price"] * data["quantity"]
    total += subtotal
    print(f"{item}: {data['quantity']} x {data['price']:.2f} = {subtotal:.2f}")

print(f"\nTotal: {total:.2f}")