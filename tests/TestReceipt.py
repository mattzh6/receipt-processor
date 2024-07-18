import unittest
from model.Receipt import Receipt
from model.Item import Item
from pydantic import ValidationError

class TestReceipt(unittest.TestCase):
    def testGoodReceipt(self):
        receipt = {
            "retailer": "Walmart",
            "purchaseDate": "2021-01-01",
            "purchaseTime": "12:00",
            "items": [
                {"shortDescription": "Milk", "price": "2.99"},
                {"shortDescription": "Bread", "price": "1.99"},
            ],
            "total": "4.98",
        }
        receipt["items"] = [Item(**item) for item in receipt["items"]]
        receipt = Receipt(**receipt)
        self.assertEqual("Walmart", receipt.getRetailer)
        self.assertEqual("2021-01-01", receipt.getPurchaseDate)
        self.assertEqual("12:00", receipt.getPurchaseTime)
        self.assertEqual(2, len(receipt.getItems))
        self.assertEqual("Milk", receipt.getItems[0].getShortDescription)
        self.assertEqual("2.99", receipt.getItems[0].getPrice)
        self.assertEqual("Bread", receipt.getItems[1].getShortDescription)
        self.assertEqual("1.99", receipt.getItems[1].getPrice)
        self.assertEqual("4.98", receipt.getTotal)

    def testBadRetailer(self):
        with self.assertRaises(ValidationError):
            receipt = {
                "retailer": "!Walmart!",
                "purchaseDate": "2021-01-01",
                "purchaseTime": "12:00",
                "items": [
                    {"shortDescription": "Milk", "price": "2.99"},
                    {"shortDescription": "Bread", "price": "1.99"},
                ],
                "total": "4.98",
            }
            receipt["items"] = [Item(**item) for item in receipt["items"]]
            Receipt(**receipt)

    def testMissingRetailer(self):
        with self.assertRaises(ValidationError):
            receipt = {
                "purchaseDate": "2021-01-01",
                "purchaseTime": "12:00",
                "items": [
                    {"shortDescription": "Milk", "price": "2.99"},
                    {"shortDescription": "Bread", "price": "1.99"},
                ],
                "total": "4.98",
            }
            receipt["items"] = [Item(**item) for item in receipt["items"]]
            Receipt(**receipt)

    def testBadPurchaseDate(self):
        with self.assertRaises(ValidationError):
            receipt = {
                "retailer": "Walmart",
                "purchaseDate": "2021a-012-012",
                "purchaseTime": "12:00",
                "items": [
                    {"shortDescription": "Milk", "price": "2.99"},
                    {"shortDescription": "Bread", "price": "1.99"},
                ],
                "total": "4.98",
            }
            receipt["items"] = [Item(**item) for item in receipt["items"]]
            Receipt(**receipt)

    def testMissingPurchaseDate(self):
        with self.assertRaises(ValidationError):
            receipt = {
                "retailer": "Walmart",
                "purchaseTime": "12:00",
                "items": [
                    {"shortDescription": "Milk", "price": "2.99"},
                    {"shortDescription": "Bread", "price": "1.99"},
                ],
                "total": "4.98",
            }
            receipt["items"] = [Item(**item) for item in receipt["items"]]
            Receipt(**receipt)

    def testBadPurchaseTime(self):
        with self.assertRaises(ValidationError):
            receipt = {
                "retailer": "Walmart",
                "purchaseDate": "2021-01-01",
                "purchaseTime": "12:0a",
                "items": [
                    {"shortDescription": "Milk", "price": "2.99"},
                    {"shortDescription": "Bread", "price": "1.99"},
                ],
                "total": "4.98",
            }
            receipt["items"] = [Item(**item) for item in receipt["items"]]
            Receipt(**receipt)

    def testMissingPurchaseTime(self):
        with self.assertRaises(ValidationError):
            receipt = {
                "retailer": "Walmart",
                "purchaseDate": "2021-01-01",
                "items": [
                    {"shortDescription": "Milk", "price": "2.99"},
                    {"shortDescription": "Bread", "price": "1.99"},
                ],
                "total": "4.98",
            }
            receipt["items"] = [Item(**item) for item in receipt["items"]]
            Receipt(**receipt)

    def testEmptyItems(self):
        with self.assertRaises(ValidationError):
            receipt = {
                "retailer": "Walmart",
                "purchaseDate": "2021-01-01",
                "purchaseTime": "12:00",
                "items": [],
                "total": "4.98",
            }
            Receipt(**receipt)

    def testMissingItems(self):
        with self.assertRaises(ValidationError):
            receipt = {
                "retailer": "Walmart",
                "purchaseDate": "2021-01-01",
                "purchaseTime": "12:00",
                "total": "4.98",
            }
            Receipt(**receipt)

    def testBadTotal(self):
        with self.assertRaises(ValidationError):
            receipt = {
                "retailer": "Walmart",
                "purchaseDate": "2021-01-01",
                "purchaseTime": "12:00",
                "items": [
                    {"shortDescription": "Milk", "price": "2.99"},
                    {"shortDescription": "Bread", "price": "1.99"},
                ],
                "total": "4.a!",
            }
            receipt["items"] = [Item(**item) for item in receipt["items"]]
            Receipt(**receipt)

    def testMissingTotal(self):
        with self.assertRaises(ValidationError):
            receipt = {
                "retailer": "Walmart",
                "purchaseDate": "2021-01-01",
                "purchaseTime": "12:00",
                "items": [
                    {"shortDescription": "Milk", "price": "2.99"},
                    {"shortDescription": "Bread", "price": "1.99"},
                ],
            }
            receipt["items"] = [Item(**item) for item in receipt["items"]]
            Receipt(**receipt)