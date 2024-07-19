import unittest
from receipt_processing_app.controller.in_memory_database_controller import (
    InMemoryDatabaseController,
)
from receipt_processing_app.model.receipt import Receipt
from receipt_processing_app.model.item import Item


class TestInMemoryDatabaseController(unittest.TestCase):

    def test_create_receipt(self):
        in_memory_database_controller = InMemoryDatabaseController()
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
        receipt_id = in_memory_database_controller.create_receipt(receipt)
        returnedReceipt = in_memory_database_controller.get_receipt(receipt_id)
        self.assertEqual(receipt.retailer, returnedReceipt.retailer)
        self.assertEqual(receipt.purchase_date, returnedReceipt.purchase_date)
        self.assertEqual(receipt.purchase_time, returnedReceipt.purchase_time)
        self.assertEqual(receipt.total, returnedReceipt.total)
        self.assertListEqual(receipt.items, returnedReceipt.items)

    def test_nonexistent_receipt_id(self):
        in_memory_database_controller = InMemoryDatabaseController()
        with self.assertRaises(ValueError):
            in_memory_database_controller.get_receipt("this id should not work")
