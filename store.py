import products


class Store:
    def __init__(self):
        self.products = []

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
        all_products = []
        for product in self.products:
            if product.is_active():
                all_products.append(product)
        return all_products

    def order(self, shopping_list):
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

bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)

# instance of a store
best_buy = Store()

pixel = products.Product("Google Pixel 7", price=500, quantity=250)
best_buy.add_product(pixel)
best_buy.add_product(bose)
best_buy.add_product(mac)




product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                 ]

products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))







