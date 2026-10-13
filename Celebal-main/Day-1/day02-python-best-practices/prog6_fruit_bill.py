# Program 6: Fruit Bill Generation App

APPLE_GST_RATE = 0.12
ORANGE_GST_RATE = 0.05

buyer_name = input("Enter Buyer Name: ").strip()
apple_price = float(input("Enter Apple price per kg: "))
apple_quantity = float(input("Enter Apple Quantity in kg: "))
orange_price = float(input("Enter Orange price per kg: "))
orange_quantity = float(input("Enter Orange Quantity in kg: "))

apple_subtotal = apple_price * apple_quantity
apple_gst = apple_subtotal * APPLE_GST_RATE
apple_total = apple_subtotal + apple_gst

orange_subtotal = orange_price * orange_quantity
orange_gst = orange_subtotal * ORANGE_GST_RATE
orange_total = orange_subtotal + orange_gst

grand_total = apple_total + orange_total

line = "-" * 83
print(f"\nBuyer Name: {buyer_name}")
print(line)
print(
    f"| {'Item Code':^12} | {'Price/Unit':^10} | {'# unit':^8} | "
    f"{'Price':^12} | {'GST':^10} | {'Total w/ GST':^14} |"
)
print(line)
print(
    f"| {'Apple':^12} | Rs {apple_price:<7.2f} | {apple_quantity:>8.1f} | "
    f"Rs {apple_subtotal:>9.2f} | Rs {apple_gst:>7.2f} | Rs {apple_total:>11.2f} |"
)
print(
    f"| {'Orange':^12} | Rs {orange_price:<7.2f} | {orange_quantity:>8.1f} | "
    f"Rs {orange_subtotal:>9.2f} | Rs {orange_gst:>7.2f} | Rs {orange_total:>11.2f} |"
)
print(line)
print(f"Total{'₹ ' + format(grand_total, '.2f'):>{len(line) - 5}}")
print(f"Total Round{'₹ ' + format(round(grand_total), '.2f'):>{len(line) - 10}}")
print(line)
