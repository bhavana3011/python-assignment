
# Smart Canteen Order and Stock Management

# Item prices and available stock
menu = {
    "Birynai": [320, 10],
    "Staters": [190, 5],
    "Desserts": [180, 8]
}

total_sales = 0

# Process customer orders
while True:
    print("\n--- Canteen Menu ---")

    for item in menu:
        print(item, "- Rs.", menu[item][0],
              "| Stock:", menu[item][1])

    choice = input("\nEnter item name (or 'stop' to finish): ").title()

    if choice == "Stop":
        break

    if choice not in menu:
        print("Item not available!")
        continue

    quantity = int(input("Enter quantity: "))

    # Check available stock
    if quantity <= 0:
        print("Please enter a valid quantity.")
    elif quantity > menu[choice][1]:
        print("Insufficient stock! Order rejected.")
    else:
        bill = menu[choice][0] * quantity

        # Update stock and sales
        menu[choice][1] -= quantity
        total_sales += bill

        print("Order successful!")
        print("Bill amount: Rs.", bill)

# Display daily summary
print("\n--- Daily Canteen Summary ---")
print("Total Sales: Rs.", total_sales)
print("Remaining Stock:")

for item in menu:
    print(item, ":", menu[item][1])

print("Thank you!")
