import unittest
from datetime import time
from controller import ReceiptProcessingService
from model.Item import Item
from model.Receipt import Receipt

class TestReceiptProcessingService(unittest.TestCase):

    def test_alphanumeric_count(self):
        receipt_processing_service = ReceiptProcessingService.ReceiptProcessingService()
        self.assertEqual(receipt_processing_service.alphanumeric_count("Target"), 6)
        self.assertEqual(receipt_processing_service.alphanumeric_count("M&M Corner Market"), 14)
        self.assertEqual(receipt_processing_service.alphanumeric_count("?><$#  #\n\t"), 0)
        self.assertEqual(receipt_processing_service.alphanumeric_count(""), 0)

    def test_total_round_dollar(self):
        receipt_processing_service = ReceiptProcessingService.ReceiptProcessingService()
        self.assertEqual(receipt_processing_service.total_round_dollar("9.00"), 50)
        self.assertEqual(receipt_processing_service.total_round_dollar("4.50"), 0)
        self.assertEqual(receipt_processing_service.total_round_dollar("0.00"), 0)

    def test_total_multiple(self):
        receipt_processing_service = ReceiptProcessingService.ReceiptProcessingService()
        self.assertEqual(receipt_processing_service.total_multiple("35.35"), 0)
        self.assertEqual(receipt_processing_service.total_multiple("0.00"), 0)
        self.assertEqual(receipt_processing_service.total_multiple("9.00"), 25)
        self.assertEqual(receipt_processing_service.total_multiple("156.25"), 25)
        self.assertEqual(receipt_processing_service.total_multiple("56.50"), 25)
        self.assertEqual(receipt_processing_service.total_multiple("6.75"), 25)

    def test_every_two_items(self):
        receipt_processing_service = ReceiptProcessingService.ReceiptProcessingService()

        items_one = [
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
        items_one = [Item(**item) for item in items_one]
        self.assertEqual(receipt_processing_service.every_two_items(items_one), 10)
        self.assertEqual(receipt_processing_service.every_two_items([]), 0)

        items_two = [
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
        items_two = [Item(**item) for item in items_two]
        self.assertEqual(receipt_processing_service.every_two_items(items_two), 10)

    def test_description_multiple(self):
        receipt_processing_service = ReceiptProcessingService.ReceiptProcessingService()
        items_one = [
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
        items_one = [Item(**item) for item in items_one]
        self.assertEqual(receipt_processing_service.description_multiple(items_one), 6)

        items_two = [
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
        items_two = [Item(**item) for item in items_two]
        self.assertEqual(receipt_processing_service.description_multiple(items_two), 0)

    def test_odd_purchase_date(self):
        receipt_processing_service = ReceiptProcessingService.ReceiptProcessingService()
        self.assertEqual(receipt_processing_service.odd_purchase_date("2022-01-01"), 6)
        self.assertEqual(receipt_processing_service.odd_purchase_date("2022-01-02"), 0)

    def test_purchase_time(self):
        receipt_processing_service = ReceiptProcessingService.ReceiptProcessingService()
        start = time(14, 0, 0)
        end = time(16, 0, 0)
        self.assertEqual(receipt_processing_service.purchase_time(start, end, "14:01"), 10)
        self.assertEqual(receipt_processing_service.purchase_time(start, end, "15:33"), 10)
        self.assertEqual(receipt_processing_service.purchase_time(start, end, "14:00"), 0)
        self.assertEqual(receipt_processing_service.purchase_time(start, end, "16:00"), 0)
        self.assertEqual(receipt_processing_service.purchase_time(start, end, "03:43"), 0)

    def test_calculate_points(self):

        receipt_processing_service = ReceiptProcessingService.ReceiptProcessingService()
        receipt_one = {
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
        receipt_one = Receipt(**receipt_one)
        receipt_two = {
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
        receipt_two = Receipt(**receipt_two)
        self.assertEqual(receipt_processing_service.calculate_points(receipt_one), 28)
        self.assertEqual(receipt_processing_service.calculate_points(receipt_two), 109)