class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f'{self.name} - ${self.price:.2f} (Stock: {self.stock})'
    
class Order:
    def __init__(self):
        self.items = []
        self.discount = 0

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            product.stock -= quantity
            self.items.append((product, quantity))
            print(f'Added {quantity}x {product.name} to order.')
        else:
            print(f'Not enough stock for {product.name}.')

    def apply_discount(self, percent):
        if 0 <= percent <= 100:
            self.discount = percent
            print(f'Discount applied: {percent}%')
        else:
            print('Invalid discount value.')

    @property
    def get_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity

        if self.discount > 0:
            total -= total * (self.discount / 100)

        return total
    
    @property
    def print_invoice(self):
        print()
        for product, quantity in self.items:
            print(f'{quantity}x {product.name} @ ${product.price:.2f} = ${product.price * quantity:.2f}')
        print(f"Discount: {self.discount}%")
        print(f"Total: ${self.get_total:.2f}")

p1 = Product("Laptop", 1200, 5)
p2 = Product("Mouse", 25, 50)
p3 = Product("Keyboard", 75, 20)

order = Order()

order.add_product(p1, 1)
order.add_product(p2, 2)
order.add_product(p3, 1)

order.apply_discount(10)

order.print_invoice