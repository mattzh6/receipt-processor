import unittest
from receiptProcessingApp.model.receipt import Receipt
from receiptProcessingApp.model.item import Item
from pydantic import ValidationError

class TestReceipt(unittest.TestCase):
    def test_good_receipt(self):
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
        self.assertEqual("Walmart", receipt.retailer)
        self.assertEqual("2021-01-01", receipt.purchase_date)
        self.assertEqual("12:00", receipt.purchase_time)
        self.assertEqual(2, len(receipt.items))
        self.assertEqual("Milk", receipt.items[0].short_description)
        self.assertEqual("2.99", receipt.items[0].price)
        self.assertEqual("Bread", receipt.items[1].short_description)
        self.assertEqual("1.99", receipt.items[1].price)
        self.assertEqual("4.98", receipt.total)

    def test_bad_retailer(self):
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

    def test_missing_retailer(self):
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

    def test_bad_purchaseDate(self):
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

    def test_missing_purchaseDate(self):
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

    def test_bad_purchase_time(self):
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

    def test_missing_purchase_time(self):
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

    def test_empty_items(self):
        with self.assertRaises(ValidationError):
            receipt = {
                "retailer": "Walmart",
                "purchaseDate": "2021-01-01",
                "purchaseTime": "12:00",
                "items": [],
                "total": "4.98",
            }
            Receipt(**receipt)

    def test_missing_items(self):
        with self.assertRaises(ValidationError):
            receipt = {
                "retailer": "Walmart",
                "purchaseDate": "2021-01-01",
                "purchaseTime": "12:00",
                "total": "4.98",
            }
            Receipt(**receipt)

    def test_bad_total(self):
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

    def test_missing_total(self):
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