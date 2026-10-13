# Self Practice 8: Retail Invoicing App

HOUSEHOLD_GST_RATE = 0.05
PROCESSED_FOOD_GST_RATE = 0.12

buyer_name = input("Enter Buyer Name: ").strip()
household_price = float(input("Enter Household Good Price: "))
household_quantity = float(input("Enter Household Good Quantity: "))
food_price = float(input("Enter Processed Food price: "))
food_quantity = float(input("Enter Processed Food Quantity: "))

household_subtotal = household_price * household_quantity
household_gst = household_subtotal * HOUSEHOLD_GST_RATE
household_total = household_subtotal + household_gst

food_subtotal = food_price * food_quantity
food_gst = food_subtotal * PROCESSED_FOOD_GST_RATE
food_total = food_subtotal + food_gst

grand_total = household_total + food_total
line = "-" * 82

print(f"\nBuyer Name: {buyer_name}")
print(line)
print(
    f"| {'Item Code':^16} | {'Price/Unit':^10} | {'#unit':^7} | "
    f"{'Price':^11} | {'GST':^9} | {'Total w/ GST':^13} |"
)
print(line)
print(
    f"| {'Household Good':^16} | Rs {household_price:<7.2f} | "
    f"{household_quantity:>7.1f} | Rs {household_subtotal:>8.2f} | "
    f"Rs {household_gst:>6.2f} | Rs {household_total:>10.2f} |"
)
print(
    f"| {'Processed Food':^16} | Rs {food_price:<7.2f} | "
    f"{food_quantity:>7.1f} | Rs {food_subtotal:>8.2f} | "
    f"Rs {food_gst:>6.2f} | Rs {food_total:>10.2f} |"
)
print(line)
print(f"Total{'₹ ' + format(grand_total, '.2f'):>{len(line) - 5}}")
print(f"Total Round{'₹ ' + format(round(grand_total), '.2f'):>{len(line) - 10}}")
print(line)
