import unittest
from datetime import time
from receiptProcessingApp.controller.ReceiptProcessingService import ReceiptProcessingService
from receiptProcessingApp.model.Item import Item
from receiptProcessingApp.model.Receipt import Receipt

class TestReceiptProcessingService(unittest.TestCase):

    def testAlphanumericCount(self):
        receiptProcessingService = ReceiptProcessingService()
        self.assertEqual(receiptProcessingService.alphanumericCount("Target"), 6)
        self.assertEqual(receiptProcessingService.alphanumericCount("M&M Corner Market"), 14)
        self.assertEqual(receiptProcessingService.alphanumericCount("?><$#  #\n\t"), 0)
        self.assertEqual(receiptProcessingService.alphanumericCount(""), 0)

    def testTotalRoundDollar(self):
        receiptProcessingService = ReceiptProcessingService()
        self.assertEqual(receiptProcessingService.totalRoundDollar("9.00"), 50)
        self.assertEqual(receiptProcessingService.totalRoundDollar("4.50"), 0)
        self.assertEqual(receiptProcessingService.totalRoundDollar("0.00"), 0)

    def testTotalMultiple(self):
        receiptProcessingService = ReceiptProcessingService()
        self.assertEqual(receiptProcessingService.totalMultiple("35.35"), 0)
        self.assertEqual(receiptProcessingService.totalMultiple("0.00"), 0)
        self.assertEqual(receiptProcessingService.totalMultiple("9.00"), 25)
        self.assertEqual(receiptProcessingService.totalMultiple("156.25"), 25)
        self.assertEqual(receiptProcessingService.totalMultiple("56.50"), 25)
        self.assertEqual(receiptProcessingService.totalMultiple("6.75"), 25)

    def testEveryTwoItems(self):
        receiptProcessingService = ReceiptProcessingService()

        firstItems = [
            {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6.49"
            }, {
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
            }, {
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
            }, {
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
            }, {
                "shortDescription": "    Klarbrunn 12-PK 12 FL OZ      ",
                "price": "12.00"
            }
        ]
        firstItems = [Item(**item) for item in firstItems]
        self.assertEqual(receiptProcessingService.everyTwoItems(firstItems), 10)
        self.assertEqual(receiptProcessingService.everyTwoItems([]), 0)

        secondItems = [
            {
                "shortDescription": "Gatorade",
                "price": "2.25"
            }, {
                "shortDescription": "Gatorade",
                "price": "2.25"
            }, {
                "shortDescription": "Gatorade",
                "price": "2.25"
            }, {
                "shortDescription": "Gatorade",
                "price": "2.25"
            }
        ]
        secondItems = [Item(**item) for item in secondItems]
        self.assertEqual(receiptProcessingService.everyTwoItems(secondItems), 10)

    def test_description_multiple(self):
        receiptProcessingService = ReceiptProcessingService()
        firstItems = [
            {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6.49"
            }, {
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
            }, {
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
            }, {
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
            }, {
                "shortDescription": "    Klarbrunn 12-PK 12 FL OZ      ",
                "price": "12.00"
            }
        ]
        firstItems = [Item(**item) for item in firstItems]
        self.assertEqual(receiptProcessingService.descriptionMultiple(firstItems), 6)

        secondItems = [
            {
                "shortDescription": "Gatorade",
                "price": "2.25"
            }, {
                "shortDescription": "Gatorade",
                "price": "2.25"
            }, {
                "shortDescription": "Gatorade",
                "price": "2.25"
            }, {
                "shortDescription": "Gatorade",
                "price": "2.25"
            }
        ]
        secondItems = [Item(**item) for item in secondItems]
        self.assertEqual(receiptProcessingService.descriptionMultiple(secondItems), 0)

    def test_odd_purchase_date(self):
        receiptProcessingService = ReceiptProcessingService()
        self.assertEqual(receiptProcessingService.oddPurchaseDate("2022-01-01"), 6)
        self.assertEqual(receiptProcessingService.oddPurchaseDate("2022-01-02"), 0)

    def test_purchase_time(self):
        receiptProcessingService = ReceiptProcessingService()
        start = time(14, 0, 0)
        end = time(16, 0, 0)
        self.assertEqual(receiptProcessingService.purchaseTime(start, end, "14:01"), 10)
        self.assertEqual(receiptProcessingService.purchaseTime(start, end, "15:33"), 10)
        self.assertEqual(receiptProcessingService.purchaseTime(start, end, "14:00"), 0)
        self.assertEqual(receiptProcessingService.purchaseTime(start, end, "16:00"), 0)
        self.assertEqual(receiptProcessingService.purchaseTime(start, end, "03:43"), 0)

    def test_calculate_points(self):

        receiptProcessingService = ReceiptProcessingService()
        firstReceipt = {
          "retailer": "Target",
          "purchaseDate": "2022-01-01",
          "purchaseTime": "13:01",
          "items": [
            {
              "shortDescription": "Mountain Dew 12PK",
              "price": "6.49"
            },{
              "shortDescription": "Emils Cheese Pizza",
              "price": "12.25"
            },{
              "shortDescription": "Knorr Creamy Chicken",
              "price": "1.26"
            },{
              "shortDescription": "Doritos Nacho Cheese",
              "price": "3.35"
            },{
              "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
              "price": "12.00"
            }
          ],
          "total": "35.35"
        }
        firstReceipt = Receipt(**firstReceipt)
        secondReceipt = {
          "retailer": "M&M Corner Market",
          "purchaseDate": "2022-03-20",
          "purchaseTime": "14:33",
          "items": [
            {
              "shortDescription": "Gatorade",
              "price": "2.25"
            },{
              "shortDescription": "Gatorade",
              "price": "2.25"
            },{
              "shortDescription": "Gatorade",
              "price": "2.25"
            },{
              "shortDescription": "Gatorade",
              "price": "2.25"
            }
          ],
          "total": "9.00"
        }
        secondReceipt = Receipt(**secondReceipt)
        self.assertEqual(receiptProcessingService.calculatePoints(firstReceipt), 28)
        self.assertEqual(receiptProcessingService.calculatePoints(secondReceipt), 109)