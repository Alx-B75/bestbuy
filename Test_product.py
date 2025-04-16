import pytest
from products import Product, NonStockedProduct, PercentageDiscount, SecondItemHalfPrice, Buy2Get1Free


def test_product():
    product = Product("iPhone", price=999, quantity=10)

    assert product.name == "iPhone"
    assert product.price == 999
    assert product.quantity == 10

def test_product_empty_name_exception():
    with pytest.raises(ValueError):
        Product("", price= 1450, quantity= 100)

def test_negative_price_raises_exception():
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price= -150, quantity= 100)

def test_is_inactive_zero_stock():
    product = Product("Promo Item", price = 0, quantity = 0)
    assert product.active is False

def test_purchase_decreases_stock():
    product = Product("Promo Item", price = 10, quantity = 10)
    total = product.buy(3)
    assert product.quantity == 7
    assert total == 30

def test_stock_cannot_be_negative():
    product = Product("Promo Item", price = 10, quantity = 10)
    result = product.buy(15)
    assert result == 0
    assert product.quantity == 10

def test_non_stocked_products_work_as_expected():
    product = NonStockedProduct("Windows License", price = 99)

    assert product.name == "Windows License"
    assert product.price == 99
    assert product.quantity == 0
    assert product.active is True

    result = product.buy(3)
    assert result == 297
    assert product.quantity == 0

def test_buy_with_promotion_applied():
    promo = PercentageDiscount("20% off", 20)
    product = Product("MacBook Air M2", price=150, quantity=100, promotion=promo)
    result = product.buy(2)
    assert result == 240
    assert product.quantity == 98

def test_second_item_half_price_applied():
    promo = SecondItemHalfPrice("Second item half price")
    product = Product("Notebook", price=30, quantity=10, promotion=promo)
    total = product.buy(3)
    # 30 (full) + 15 (half) + 30 (full) = 75
    assert total == 75

def test_buy2_get1_free_applied():
    promo = Buy2Get1Free("Buy 2 Get 1 Free")
    product = Product("Pen Pack", price=15, quantity=10, promotion=promo)
    total = product.buy(6)
    # Should pay for 4 (2 sets of 3 = 2 free) → 4 * 15 = 60
    assert total == 60





