

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True if quantity > 0 else False

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            print("Quantity cannot be negative.")
            return
        self.quantity = quantity
        if self.quantity == 0:
            self.active = self.quantity > 0

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        product_details = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        return product_details

    def buy(self, quantity):
        if quantity > self.quantity:
            print(f"Not enough stock to buy {quantity} {self.name}. {self.quantity} available to sell.")
            return 0
        self.quantity -= quantity
        buy_price = self.price * quantity
        if self.quantity == 0:
            self.active = False
        return buy_price


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())

if __name__ == '__main__':
    main()

