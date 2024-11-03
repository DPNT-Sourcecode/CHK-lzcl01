prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10
}

# Sorted by number of items descending
special_offers = {
    'A': [(5, 200), (3, 130)],
    'B': [(2, 45)],
}

free_items_offers = {
    'E': (2, 'B'),
    'F': (2, 'F')
}

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
        num_frees = item_counts.get(sku, 0) // required_amount
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
