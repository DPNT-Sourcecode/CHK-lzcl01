class Price:
    def __init__(self, price, offers=None):
        self.price = price
        if offers:
            self.offers = offers
        else:
            self.offers = []
    
    def apply_offers(self, basket):
        for offer in self.offers:
            offer.apply(basket)


class SpecialOffer:
    """Shared interface for all special offer"""
    def apply(basket):

        total_price = 0

        if self.offer:
            special_price_items = purchase_count // self.offer.item_count
            regular_price_items = purchase_count % self.offer.item_count
            total_price = special_price_items * self.offer.special_price + regular_price_items * self.price
        else:
            total_price = purchase_count * self.price


class SpecialPriceOffer(SpecialOffer):
    def __init__(self, item_count, special_price):
        self.item_count = item_count
        self.special_price = special_price

    def apply(basket):
        pass

class FreeItemOffer(SpecialOffer):
    def __init__(self, target_item, item_count, free_item):
        self.target_item = target_item
        self.item_count = item_count
        self.free_item = free_item

    def apply(basket):
        pass


class Basket:
    def __init__(self, price_table):
        self.price_table = price_table
        self.item_counts = {}
        self.free_sku_counts = {}
        self.unbulked_items = {}

    def add_item(self, item):
        if item in self.sku_counts:
            self.item_counts[item] += 1
        else:
            self.item_counts[item] = 1
            self.free_item_counts[item] = 0

    def add_free_sku_eligibility(self, free_item):
        if free_item in self.free_item_counts:
            self.free_item_counts[free_item] = 1
        else:
            self.free_item_counts[free_item] += 1

    def total(self):
        
        for item in self.item_counts:
            

        return 0

price_table = {
    'A': Price(50, [SpecialOffer(3, 130), ]),
    'B': Price(30, [SpecialOffer(2, 45), ]),
    'C': Price(20),
    'D': Price(15),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = Basket()
    for sku in skus:
        if sku not in price_table:
            return -1
        
        basket.add_sku(sku)

    return basket.total()
