from uuid import uuid4

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Order:
    def __init__(self, customer, products):
        self.order_id = uuid4()
        self.customer = customer
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        return sum(p.price for p in self.products)

    def display_details(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer.name)
        print("Customer Email:", self.customer.email)

        print("Product List:")
        for p in self.products:
            print(p.name, "-", p.price)

        print("Total Order Price:", self.total_price())


# Example Usage
cust = Customer("Alice", "alice@example.com")

items = [
    Product("Book", 300),
    Product("Pen", 20)
]

order = Order(cust, items)

# Add another product
order.add_product(Product("Notebook", 100))

# Display order details
order.display_details()