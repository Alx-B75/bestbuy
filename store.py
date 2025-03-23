
class Store:
    """A class representing a store that manages products and orders."""
    def __init__(self, products=None):
        if products is None:
            self.products = []
        else:
            self.products = products

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
            print(f"{product.name} added to store.")
        else:
            print(f"{product.name} already in store.")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"{product.name} removed from store.")
        else:
            print(f"{product.name} not in store.")

    def get_total_quantity(self):
        total_products = 0
        for product in self.products:
            total_products += product.quantity
        return total_products

    def get_all_products(self):
        """Returns a list of all active products currently in stock."""
        all_products = []
        for product in self.products:
            if product.is_active():
                all_products.append(product)
        return all_products

    def order(self, shopping_list):
        """
        Processes an order for multiple products.
        Args:
            shopping_list (list): A list of tuples containing (Product, quantity).
        Returns:
            float: The total cost of the processed order.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if product in self.products:
                if product.get_quantity() >= quantity:
                    total_price += product.buy(quantity)
                else:
                    print(f"Not enough stock for {product.name}. Only {product.get_quantity()} available.")
            else:
                print(f"{product.name} is not available in the store.")

        return total_price







