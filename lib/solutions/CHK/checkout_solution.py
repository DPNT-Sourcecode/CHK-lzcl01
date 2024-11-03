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
    | A    | 50    | 3A for 130, 5A for 200          |
    | B    | 30    | 2B for 45                       |
    | C    | 20    |                                 |
    | D    | 15    |                                 |
    | E    | 40    | 2E get one B free               |
    | F    | 10    | 2F get one F free               |
    | G    | 20    |                                 |
    | H    | 10    | 5H for 45, 10H for 80           |
    | I    | 35    |                                 |
    | J    | 60    |                                 |
    | K    | 70    | 2K for 120                      |
    | L    | 90    |                                 |
    | M    | 15    |                                 |
    | N    | 40    | 3N get one M free               |
    | O    | 10    |                                 |
    | P    | 50    | 5P for 200                      |
    | Q    | 30    | 3Q for 80                       |
    | R    | 50    | 3R get one Q free               |
    | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | U    | 40    | 3U get one U free               |
    | V    | 50    | 2V for 90, 3V for 130           |
    | W    | 20    |                                 |
    | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
"""

prices = {}
special_offers = {}
free_items_offers = {}
deals = {}

def parse_shop():
    for line in table.strip().split("\n"):
        colums = line.strip().split("|")

        item = colums[1].strip()
        price = int(colums[2].strip())

        prices[item] = price
        
        if 'buy any' in colums[3]:
            tokens = colums[3].split()
            amount = int(tokens[2])
            bundle_key = tuple(sorted(tokens[4][1:-1].split(',')))
            price = int(tokens[-1])
            deals[bundle_key] = (amount, price)
            continue

        offers = colums[3].split(",")   

        for offer in offers:
            tokens = offer.split()
            if 'for' in tokens:
                amount = int(tokens[0][:-1])
                price = int(tokens[-1])
                
                if item not in special_offers:
                    special_offers[item] = []
                special_offers[item].append((amount, price))

            elif 'get' in tokens:
                amount = int(tokens[0][:-1])
                free_item = tokens[-2]
                free_items_offers[item] = (amount, free_item)


    for offers in special_offers.values():
        offers.sort(reverse=True)


def most_expensive_first(sku):
    return -prices[sku]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total_price = 0

    if not prices:
        print("Hello")
        parse_shop()

    # Count items in basket    
    item_counts = {}
    for sku in skus:
        if sku not in prices:
            return -1
        item_counts[sku] = item_counts.get(sku, 0) + 1

    # Process deals
    for bundle, deal in deals.items():
        amount, deal_price = deal
        items = sorted(list(bundle), key=most_expensive_first)

        total_count = 0
        for item in items:
            total_count += item_counts.get(item, 0)

        num_deals = total_count // amount

        sub_amount = num_deals * amount

        for item in items:
            if item not in item_counts:
                continue
            if sub_amount <= item_counts[item]:
                item_counts[item] -= sub_amount
                break
            sub_amount -= item_counts[item]
            item_counts[item] = 0

        total_price += num_deals * deal_price

    # Count free items
    free_item_counts = {}
    for sku, offer in free_items_offers.items():
        required_amount, free_item = offer
        if sku != free_item:
            num_frees = item_counts.get(sku, 0) // required_amount
        else:
            num_frees = item_counts.get(sku, 0) // (required_amount + 1)
        free_item_counts[free_item] = free_item_counts.get(free_item, 0) + num_frees


    for sku, count in item_counts.items():
        count -= free_item_counts.get(sku, 0)

        sp_offers = special_offers.get(sku, [])
        sp_offers.append((1, prices[sku]))

        for bulk_amount, bulk_price in sp_offers:
            num_bulks = count // bulk_amount
            count = count % bulk_amount
            total_price += num_bulks * bulk_price

    return total_price







