import products
import store

def start(store_obj):
        def list_products():
            print("\nProducts available in store:")
            for product in store_obj.get_all_products():
                print(f"- {product.show()}")
            print()

        def show_total_quantity():
            total = store_obj.get_total_quantity()
            print(f"\nTotal quantity in store: {total}\n")

        def make_order():
            print("\n--- Make an Order ---")
            shopping_list = []
            for product in store_obj.get_all_products():
                print(f"{product.name} (Available: {product.get_quantity()})")
                qty = int(input(f"How many '{product.name}' would you like to buy? Enter 0 to skip: "))
                if qty > 0:
                    shopping_list.append((product, qty))
            total = store_obj.order(shopping_list)
            print(f"\nTotal order price: {total}\n")

        def quit_store():
            print("\nGoodbye!")
            exit()

        # Dispatcher dictionary
        dispatcher = {
            "1": list_products,
            "2": show_total_quantity,
            "3": make_order,
            "4": quit_store
        }

        # Menu loop
        while True:
            print("Store Menu")
            print("  ----------")
            print("1. List all products in store")
            print("2. Show total amount in store")
            print("3. Make an order")
            print("4. Quit")
            choice = input("Please choose a number: ")

            action = dispatcher.get(choice)
            if action:
                action()
            else:
                print("\nInvalid choice. Please select 1-4.\n")

def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()