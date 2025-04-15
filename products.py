

class Product:
    """A class representing a product in the store."""


    def __init__(self, name: str, price: float, quantity: int):
        if not name or name.strip() == "":
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Product price must be a positive number")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True if quantity > 0 else False


        """
                Initializes a Product instance.
                Args:
                    name (str): The product's name.
                    price (float): The product's price.
                    quantity (int): The available quantity.
                """

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
        """Returns a formatted string with product details: name, price, and quantity."""
        product_details = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        return product_details

    def buy(self, quantity):
        """
            Processes the purchase of a product.
            Args:
                quantity (int): The number of items to purchase.
            Returns:
                float: The total price for the purchase or 0 if not enough stock.
            """
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

