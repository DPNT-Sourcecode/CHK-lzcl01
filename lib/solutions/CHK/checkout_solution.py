class SpecialOffer:
    def __init__(self, item_count, special_price):
        self.item_count = item_count
        self.special_price = special_price


special_offers = {
    'A': SpecialOffer(3, 130),
    'B': SpecialOffer(2, 45)
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    raise NotImplementedError()


