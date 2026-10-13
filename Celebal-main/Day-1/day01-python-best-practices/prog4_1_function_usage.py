# Program 4.1: Proper function usage

def calculate_total(price, quantity):
    """Calculate the total cost of purchased items."""
    total_cost = price * quantity
    return total_cost


def display_total(total_cost):
    """Display the total cost in a readable format."""
    print(f"Total cost: Rs. {total_cost:.2f}")


item_price = 50
item_quantity = 3

total = calculate_total(item_price, item_quantity)
display_total(total)