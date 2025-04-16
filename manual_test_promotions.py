from products import Product, PercentageDiscount, SecondItemHalfPrice, Buy2Get1Free

promo1 = PercentageDiscount("20% off", 20)
promo2 = SecondItemHalfPrice("Second item half price")
promo3 = Buy2Get1Free("Buy 2 Get 1 Free")

# Create products with those promotions
p1 = Product("T-Shirt", price=50, quantity=10, promotion=promo1)
p2 = Product("Notebook", price=30, quantity=10, promotion=promo2)
p3 = Product("Pen Pack", price=15, quantity=10, promotion=promo3)

# Perform purchases
print("T-Shirt (20% off) x2:", p1.buy(2))  # Expect: 50*2*0.8 = 80
print("Notebook (2nd half price) x3:", p2.buy(3))  # Expect: 30 + 15 + 30 = 75
print("Pen Pack (Buy 2 Get 1 Free) x6:", p3.buy(6))  # Expect: pay for 4 = 4*15 = 60
