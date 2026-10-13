# Self Practice 5: Retail Invoicing App

import random

# GST rates
HOUSEHOLD_GST = 0.05
PROCESSED_FOOD_GST = 0.12

# Product names
items = [
    "Banana", "Masala", "Tomato", "Rice", "Soap",
    "Shampoo", "Biscuits", "Milk", "Bread", "Toothpaste",
    "Tea", "Cooking Oil", "Detergent", "Lentils", "Juice"
]

# Corresponding prices
prices = [
    15, 200, 10, 60, 35,
    120, 30, 32, 40, 55,
    90, 150, 85, 110, 45
]

# Corresponding GST rates
gst_rates = [
    HOUSEHOLD_GST,
    PROCESSED_FOOD_GST,
    HOUSEHOLD_GST,
    HOUSEHOLD_GST,
    HOUSEHOLD_GST,
    HOUSEHOLD_GST,
    PROCESSED_FOOD_GST,
    HOUSEHOLD_GST,
    HOUSEHOLD_GST,
    HOUSEHOLD_GST,
    PROCESSED_FOOD_GST,
    HOUSEHOLD_GST,
    HOUSEHOLD_GST,
    HOUSEHOLD_GST,
    PROCESSED_FOOD_GST
]


def generate_invoice(buyer_name):
    """Generate an invoice for three randomly selected products."""

    selected_items = random.sample(range(len(items)), 3)

    total = 0
    total_gst = 0
    invoice_rows = []

    for index in selected_items:
        item_name = items[index]
        price = prices[index]
        gst_rate = gst_rates[index]
        quantity = random.randint(1, 5)

        item_total = price * quantity
        item_gst = item_total * gst_rate

        total += item_total
        total_gst += item_gst

        invoice_rows.append(
            (item_name, quantity, price)
        )

    # Display invoice
    print("\nRetail Invoicing App")
    print("-" * 40)
    print(f"Buyer Name: {buyer_name}")
    print("-" * 40)

    print(f"| {'Item':^15} | {'Qty':^5} | {'Price':^10} |")
    print("-" * 40)

    for item_name, quantity, price in invoice_rows:
        print(
            f"| {item_name:<15} | {quantity:^5} | "
            f"{price:^10.2f} |"
        )

    print("-" * 40)
    print(f"{'Total':<25} Rs {total:>10.2f}")
    print(f"{'GST':<25} Rs {total_gst:>10.2f}")
    print("-" * 40)
    print(f"{'Total Billing':<25} Rs {total + total_gst:>10.2f}")
    print("-" * 40)


buyer_name = input("Enter the buyer name: ").strip()

if buyer_name:
    generate_invoice(buyer_name)
else:
    print("Buyer name cannot be empty.")