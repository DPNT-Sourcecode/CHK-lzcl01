# class Price:
#     def __init__(self, price, offers=None):
#         self.price = price
#         if offers:
#             self.offers = offers
#         else:
#             self.offers = []
    
#     def apply_offers(self, basket):
#         for offer in self.offers:
#             offer.apply(basket)


# class SpecialOffer:
#     """Shared interface for all special offer"""
#     def apply(basket):

#         total_price = 0

#         if self.offer:
#             special_price_items = purchase_count // self.offer.item_count
#             regular_price_items = purchase_count % self.offer.item_count
#             total_price = special_price_items * self.offer.special_price + regular_price_items * self.price
#         else:
#             total_price = purchase_count * self.price


# class SpecialPriceOffer(SpecialOffer):
#     def __init__(self, item_count, special_price):
#         self.item_count = item_count
#         self.special_price = special_price

#     def apply(basket):
#         pass

# class FreeItemOffer(SpecialOffer):
#     def __init__(self, target_item, item_count, free_item):
#         self.target_item = target_item
#         self.item_count = item_count
#         self.free_item = free_item

#     def apply(basket):
#         pass


# class Basket:
#     def __init__(self, price_table):
#         self.price_table = price_table
#         self.item_counts = {}
#         self.free_sku_counts = {}
#         self.unbulked_items = {}

#     def add_item(self, item):
#         if item in self.sku_counts:
#             self.item_counts[item] += 1
#         else:
#             self.item_counts[item] = 1
#             self.free_item_counts[item] = 0

#     def add_free_sku_eligibility(self, free_item):
#         if free_item in self.free_item_counts:
#             self.free_item_counts[free_item] = 1
#         else:
#             self.free_item_counts[free_item] += 1

#     def total(self):
        
#         for item in self.item_counts:
            
#         return 0


# price_table = {
#     'A': Price(50, [SpecialOffer(3, 130), SpecialOffer(5, 200)]),
#     'B': Price(30, [SpecialOffer(2, 45)]),
#     'C': Price(20),
#     'D': Price(15),
#     'E': Price(40, [FreeItemOffer('E', 2, 'B')])
# }

prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}

special_offers = {
    'A': [(3, 130), (5, 200)],
    'B': (2, 45),
}

free_items_offers = {
    'E': (2, 'B')
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # Count items in basket    
    item_counts = {}
    for sku in skus:
        item_counts[sku] = item_counts.get(sku, 0) + 1

    # Count free items
    free_item_counts = {}
    for sku, offer in free_items_offers.items():
        required_amount, free_item = offer
        num_frees = item_counts[sku] // required_amount
        free_item_counts[free_item] = free_item_counts.get(free_item, 0) + num_frees

    total_price = 0

    for sku, count in item_counts.items():
        

    return total_price





