import unittest
from controller.InMemoryDatabaseController import InMemoryDatabaseController
from model.Receipt import Receipt
from model.Item import Item

class TestInMemoryDatabaseController(unittest.TestCase):

    def testCreateReceipt(self):
        inMemoryDatabaseController = InMemoryDatabaseController()
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
        receiptId = inMemoryDatabaseController.createReceipt(receipt)
        returnedReceipt = inMemoryDatabaseController.getReceipt(receiptId)
        self.assertEqual(receipt.getRetailer, returnedReceipt.getRetailer)
        self.assertEqual(receipt.getPurchaseDate, returnedReceipt.getPurchaseDate)
        self.assertEqual(receipt.getPurchaseTime, returnedReceipt.getPurchaseTime)
        self.assertEqual(receipt.getTotal, returnedReceipt.getTotal)
        self.assertListEqual(receipt.getItems, returnedReceipt.getItems)




    def testNonexistantReceiptId(self):
        inMemoryDatabaseController = InMemoryDatabaseController()
        with self.assertRaises(ValueError):
            inMemoryDatabaseController.getReceipt("this id should not work")