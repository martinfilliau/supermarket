import unittest

from app import Product, Checkout, buy_one_get_one


class AppTest(unittest.TestCase):

    def test_grand_total(self):
        p1 = Product("p1", "Test", 5.10)
        p2 = Product("p2", "TEST", 2.22)
        checkout = Checkout([])
        checkout.scan(p1)
        checkout.scan(p1)
        checkout.scan(p2)
        gd_total = checkout._grand_total()
        self.assertEqual(1242, gd_total)

    def test_total(self):
        p1 = Product("p1", "Test", 5.10)
        p2 = Product("p2", "TEST", 2.22)
        checkout = Checkout([buy_one_get_one])
        checkout.scan(p1)
        checkout.scan(p1)
        checkout.scan(p2)
        total = checkout.total()
        self.assertEqual(total, 1222)

    def test_get_as_dict_count(self):
        p1 = Product("p1", "Test", 5.10)
        p2 = Product("p2", "TEST", 2.22)
        checkout = Checkout([])
        checkout.scan(p1)
        checkout.scan(p1)
        checkout.scan(p2)
        counts = checkout._get_as_dict_count()
        self.assertEqual(counts['p1'], 2)
        self.assertEqual(counts['p2'], 1)

    def test_buy_one_get_one(self):
        products = {'p1': 2, 'p2': 12}
        result = buy_one_get_one(products)
        self.assertEqual(result, -20)


if __name__ == "__main__":
    unittest.main()