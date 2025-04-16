from abc import ABC, abstractmethod


class Product:
    """A class representing a product in the store."""

    def __init__(self, name: str, price: float, quantity: int, promotion=None):
        """
         Initializes a Product instance.
            Args:
                name (str): The product's name.
                price (float): The product's price.
                quantity (int): The available quantity.
                promotion (float): Promotion applied?
        """
        if not name or name.strip() == "":
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Product price must be a positive number")
        self.name = name
        self.price = price
        self.quantity = quantity
        self._active = quantity > 0
        self.promotion = promotion

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
        """
        Returns a formatted string with product details: name, price, quantity and promotion if applicable.
        """
        if self.promotion:
            product_details = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion applied: {self.promotion.name}"
        else:
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
        if self.promotion:
            buy_price = self.promotion.apply_promotion(self, quantity)
        else:
            buy_price = self.price * quantity
        if self.quantity == 0:
            self.active = False
        return buy_price

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    @property
    def active(self):
        return True

    def buy(self, quantity):
        return self.price * quantity

    def show(self):
        return super().show() + "***non-stock item***"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity <= self.maximum:
            return super().buy(quantity)
        else:
            raise ValueError(f"Cannot buy more than {self.maximum} of this item.")

    def show(self):
        return super().show() + f" (Limit: {self.maximum} per order)"


class Promotion(ABC):
    """Abstract class as base for promotions"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentageDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
           Apply the 'x percentage discount' promotion to a given product.
           Returns the total price after the discount.
           """
        return (product.price * quantity) * (1 - self.percent / 100)


class SecondItemHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
           Apply the 'second item half price' promotion to a given product.
           Returns the total price after the discount.
           """
        discounted_pairs = quantity // 2
        full_price_items = quantity % 2
        total_price = (discounted_pairs * 1.5 * product.price) + (full_price_items * product.price)
        return total_price


class Buy2Get1Free(Promotion):
    """Subclass for promotion, buy two products and get the third free"""

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
           Apply the 'Buy 2, Get 1 Free' promotion to a given product.
           Returns the total price after the discount.
           """
        free_items = quantity // 3
        paid_items = quantity - free_items
        total_price = paid_items * product.price
        return total_price
