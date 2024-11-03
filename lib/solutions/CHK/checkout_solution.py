class Price:
    def __init__(self, price, offer=None):
        self.price = price
        self.offer = offer

class SpecialOffer:
    def __init__(self, item_count, special_price):
        self.item_count = item_count
        self.special_price = special_price


special_offers = {
    'A': Price(50, SpecialOffer(3, 130)),
    'B': Price(30, SpecialOffer(2, 45)),
    'C': Price(20),
    'D': Price(15),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    raise NotImplementedError()
