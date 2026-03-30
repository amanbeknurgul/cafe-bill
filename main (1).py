# Variant D — Café Bill

customer_name = input("Enter customer name: ")

subtotal = 0.0
items_count = 0

# Task D1 — Multiple Orders
while True:
    item_name = input("Enter item name (or 'done' to finish): ")

    if item_name.lower() == "done":
        break

    price = float(input("Enter price: "))
    subtotal += price
    items_count += 1

print("Customer :", customer_name.upper())
print("Items :", items_count)
print("Subtotal :", subtotal, "KZT")

# Task D2 — Time-Based Discount
hour = int(input("Enter current hour (0-23): "))
print("------------------------------")

if 6 <= hour < 12:
    discount_label = "Morning discount"
    discount_percent = 0.10

    discount_amount = subtotal * discount_percent
    after_discount = subtotal - discount_amount
    tip = after_discount * 0.10
    total = after_discount + tip

    print("Time period :", discount_label)
    print("Discount :", discount_amount, "KZT")
    print("Tip (10%) :", tip, "KZT")
    print("Total :", total, "KZT")

elif 12 <= hour < 17:
    discount_label = "No discount"
    discount_percent = 0.0

    discount_amount = subtotal * discount_percent
    after_discount = subtotal - discount_amount
    tip = after_discount * 0.10
    total = after_discount + tip

    print("Time period :", discount_label)
    print("Discount :", discount_amount, "KZT")
    print("Tip (10%) :", tip, "KZT")
    print("Total :", total, "KZT")

elif 17 <= hour < 22:
    discount_label = "Evening discount"
    discount_percent = 0.05

    discount_amount = subtotal * discount_percent
    after_discount = subtotal - discount_amount
    tip = after_discount * 0.10
    total = after_discount + tip

    print("Time period :", discount_label)
    print("Discount :", discount_amount, "KZT")
    print("Tip (10%) :", tip, "KZT")
    print("Total :", total, "KZT")

else:
    print("Time period : Closed")
    print("Cafe is closed. No total calculated.")

print("------------------------------")

# Task D3 — Name Analysis
print("Name uppercase :", customer_name.upper())
print("Name lowercase :", customer_name.lower())
print("Name length :", len(customer_name))

if customer_name[0].upper() == "A" or customer_name[0].upper() == "S":
    print("VIP customer")
else:
    print("Regular customer")
