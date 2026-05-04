class Product:
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock

products = [
    Product("AirPods", 199.99, True),
    Product("iPhone 13", 999.99, False),
    Product("MacBook", 1299.99, True),
    Product("iPad", 499.99, True),
    Product("Apple Watch", 399.99, False)
]
total = sum(p.price for p in products if p.in_stock)
print(f"Ombordagi mahsulotlar narxi: {total}")
