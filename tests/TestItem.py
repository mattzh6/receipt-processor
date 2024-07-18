import unittest
from model.Item import Item
from pydantic import ValidationError

class TestItem(unittest.TestCase):

    def testGoodItem(self):
        item = {"shortDescription": "Pasta", "price": "12.00"}
        item = Item(**item)
        self.assertEqual(item.getShortDescription, "Pasta")
        self.assertEqual(item.getPrice, "12.00")

    def testBadShortDescription(self):
        with self.assertRaises(ValidationError):
            item = {"shortDescription": "Pasta %$#@$#", "price": "12.00"}
            item = Item(**item)

    def testMissingDescription(self):
        with self.assertRaises(ValidationError):
            item = {"price": "12.00"}
            item = Item(**item)

    def testBadPrice(self):
        with self.assertRaises(ValidationError):
            item = {"shortDescription": "Pasta", "price": "12.0003"}
            item = Item(**item)

    def testMissingPrice(self):
        with self.assertRaises(ValidationError):
            item = {"shortDescription": "Pasta"}
            item = Item(**item)