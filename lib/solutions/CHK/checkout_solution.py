class Price:
    def __init__(self, price, offer=None):
        self.price = price
        self.offer = offer

    def total(self, purchase_count):
        """Calculates the total price of multiple items
        applying special offers if present
        Returns the total price of all items"""

        total_price = 0

        if self.offer:
            special_price_items = purchase_count // self.offer.item_count
            regular_price_items = purchase_count % self.offer.item_count
            total_price = special_price_items * self.offer.special_price + regular_price_items * self.price
        else:
            total_price = purchase_count * self.price

        return total_price


class SpecialOffer:
    """Shared interface for all special offer"""
    def apply(basket):
        pass


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
        


class Basket:
    def __init__(self):
        self.sku_counts = {}
        self.free_sku_counts = {}

    def add_sku(self, sku):
        if sku in self.sku_counts:
            self.sku_counts[sku] += 1
        else:
            self.sku_counts[sku] = 1
            self.free_sku_counts[sku] = 0

    def add_free_sku_eligibility(self, free_sku):
        if free_sku in self.free_sku_counts:
            self.free_sku_counts[free_sku] = 1
        else:
            self.free_sku_counts[free_sku] += 1

    def total():
        return 0

price_table = {
    'A': Price(50, SpecialOffer(3, 130)),
    'B': Price(30, SpecialOffer(2, 45)),
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






