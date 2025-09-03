original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]


def get_price(price):
    return price if price > 0 else 0


print([get_price(price) for price in original_prices])
