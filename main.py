import products
import store


def list_products(store_obj):
    """Prints a list of all active products available in the store."""
    print("\nProducts available in store:")
    for product in store_obj.get_all_products():
        print(f"- {product.show()}")
    print()


def show_total_quantity(store_obj):
    """Displays the total number of products available in stock."""
    total = store_obj.get_total_quantity()
    print(f"\nTotal quantity in store: {total}\n")


def make_order(store_obj):
    """Allows the user to select products by index and specify quantities to order."""
    print("\n--- Make an Order ---")
    shopping_list = []

    product_dict = {}
    for ind, product in enumerate(store_obj.get_all_products(), start=1):
        product_dict[ind] = product
        print(f"{ind}. {product.name} (Available: {product.get_quantity()})")

    while True:
        try:
            choice = int(input("Enter the product number to add to your order (0 to finish): "))
            if choice == 0:
                break
            if choice not in product_dict:
                print("Invalid product number, please choose again.")
                continue

            qty = int(input(f"How many '{product_dict[choice].name}' would you like to buy? "))
            if qty > 0:
                shopping_list.append((product_dict[choice], qty))
            else:
                print("Quantity must be greater than 0.")

        except ValueError:
            print("Not valid - please enter numbers only")

    if shopping_list:
        total = store_obj.order(shopping_list)
        print(f"\nTotal order price: {total}\n")
    else:
        print("No items ordered.\n")


def quit_store():
    """Exits the program with a message."""
    print("\nGoodbye!")
    exit()


def start(store_obj):
    # Dispatcher
    dispatcher = {
        "1": list_products,
        "2": show_total_quantity,
        "3": make_order,
        "4": quit_store
    }

    # loop for the menu
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
            if choice == "4":
                action()
            else:
                action(store_obj)
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
