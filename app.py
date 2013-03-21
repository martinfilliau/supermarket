from collections import Counter


# Objects

class Product(object):

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price * 100   # convert in cents


class Checkout(object):

    def __init__(self, rules):
        """Initialise the checkout with a list of rules
        to be applied on total
        :param rules: list of rules
        """
        self.rules = set(rules)
        self.products = []

    def scan(self, product):
        self.products.append(product)

    def total(self):
        """Total price less rules applied
        """
        gd_total = self._grand_total()
        counts = self._get_as_dict_count()
        for rule in self.rules:
            gd_total += rule(counts)
        return gd_total

    def _grand_total(self):
        """Total price w/o any rule applied
        """
        count = 0
        for product in self.products:
            count += product.price
        return count

    def _get_as_dict_count(self):
        """Get the list of products as a dict with count per product
        """
        counter = Counter()
        for product in self.products:
            counter[product.id] += 1
        return counter


# Rules

def buy_one_get_one(products):
    """Returns a difference if product
    :param products: dict of products
    """
    if 'p1' in products and products['p1'] >= 2:
        return -20
    else:
        return 0
