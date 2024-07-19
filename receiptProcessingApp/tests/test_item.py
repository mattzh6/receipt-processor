import unittest
from receiptProcessingApp.model.item import Item
from pydantic import ValidationError

class TestItem(unittest.TestCase):

    def test_good_item(self):
        item = {"shortDescription": "Pasta", "price": "12.00"}
        item = Item(**item)
        self.assertEqual(item.short_description, "Pasta")
        self.assertEqual(item.price, "12.00")

    def test_bad_short_description(self):
        with self.assertRaises(ValidationError):
            item = {"shortDescription": "Pasta %$#@$#", "price": "12.00"}
            item = Item(**item)

    def test_missing_description(self):
        with self.assertRaises(ValidationError):
            item = {"price": "12.00"}
            item = Item(**item)

    def test_bad_price(self):
        with self.assertRaises(ValidationError):
            item = {"shortDescription": "Pasta", "price": "12.0003"}
            item = Item(**item)

    def test_missing_price(self):
        with self.assertRaises(ValidationError):
            item = {"shortDescription": "Pasta"}
            item = Item(**item)