# prices = {
#     'A': 50,
#     'B': 30,
#     'C': 20,
#     'D': 15,
#     'E': 40,
#     'F': 10
# }

# # Sorted by number of items descending
# special_offers = {
#     'A': [(5, 200), (3, 130)],
#     'B': [(2, 45)],
# }

# free_items_offers = {
#     'E': (2, 'B'),
#     'F': (2, 'F')
# }

table = """
    | A    | 50    | 3A for 130, 5A for 200 |
    | B    | 30    | 2B for 45              |
    | C    | 20    |                        |
    | D    | 15    |                        |
    | E    | 40    | 2E get one B free      |
    | F    | 10    | 2F get one F free      |
    | G    | 20    |                        |
    | H    | 10    | 5H for 45, 10H for 80  |
    | I    | 35    |                        |
    | J    | 60    |                        |
    | K    | 80    | 2K for 150             |
    | L    | 90    |                        |
    | M    | 15    |                        |
    | N    | 40    | 3N get one M free      |
    | O    | 10    |                        |
    | P    | 50    | 5P for 200             |
    | Q    | 30    | 3Q for 80              |
    | R    | 50    | 3R get one Q free      |
    | S    | 30    |                        |
    | T    | 20    |                        |
    | U    | 40    | 3U get one U free      |
    | V    | 50    | 2V for 90, 3V for 130  |
    | W    | 20    |                        |
    | X    | 90    |                        |
    | Y    | 10    |                        |
    | Z    | 50    |                        |
"""

prices = {}
special_offers = {}
free_items_offers = {}

for line in table.split("\n"):
    

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # Count items in basket    
    item_counts = {}
    for sku in skus:
        if sku not in prices:
            return -1
        item_counts[sku] = item_counts.get(sku, 0) + 1

    # Count free items
    free_item_counts = {}
    for sku, offer in free_items_offers.items():
        required_amount, free_item = offer
        if sku != free_item:
            num_frees = item_counts.get(sku, 0) // required_amount
        else:
            num_frees = item_counts.get(sku, 0) // (required_amount + 1)
        free_item_counts[free_item] = free_item_counts.get(free_item, 0) + num_frees

    total_price = 0

    for sku, count in item_counts.items():
        count -= free_item_counts.get(sku, 0)

        sp_offers = special_offers.get(sku, [])
        sp_offers.append((1, prices[sku]))

        for bulk_amount, bulk_price in sp_offers:
            num_bulks = count // bulk_amount
            count = count % bulk_amount
            total_price += num_bulks * bulk_price

    return total_price


