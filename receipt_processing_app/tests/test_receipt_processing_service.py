import unittest
from datetime import time
from receipt_processing_app.controller.receipt_processing_service import (
    ReceiptProcessingService,
)

from receipt_processing_app.model.item import Item
from receipt_processing_app.model.receipt import Receipt


class TestReceiptProcessingService(unittest.TestCase):

    def test_alphanumeric_count(self):
        receipt_processing_service = ReceiptProcessingService()
        self.assertEqual(receipt_processing_service.alphanumeric_count("Target"), 6)
        self.assertEqual(
            receipt_processing_service.alphanumeric_count("M&M Corner Market"), 14
        )
        self.assertEqual(
            receipt_processing_service.alphanumeric_count("?><$#  #\n\t"), 0
        )
        self.assertEqual(receipt_processing_service.alphanumeric_count(""), 0)

    def test_total_round_dollar(self):
        receipt_processing_service = ReceiptProcessingService()
        self.assertEqual(receipt_processing_service.total_round_dollar("9.00"), 50)
        self.assertEqual(receipt_processing_service.total_round_dollar("4.50"), 0)
        self.assertEqual(receipt_processing_service.total_round_dollar("0.00"), 0)
        self.assertEqual(receipt_processing_service.total_round_dollar("0.01"), 0)
        self.assertEqual(receipt_processing_service.total_round_dollar("0.99"), 0)
        self.assertEqual(receipt_processing_service.total_round_dollar("10000.99"), 0)

    def test_total_multiple(self):
        receipt_processing_service = ReceiptProcessingService()
        self.assertEqual(receipt_processing_service.total_multiple("35.35"), 0)
        self.assertEqual(receipt_processing_service.total_multiple("0.00"), 0)
        self.assertEqual(receipt_processing_service.total_multiple("9.00"), 25)
        self.assertEqual(receipt_processing_service.total_multiple("156.25"), 25)
        self.assertEqual(receipt_processing_service.total_multiple("56.50"), 25)
        self.assertEqual(receipt_processing_service.total_multiple("6.75"), 25)

    def test_every_two_items(self):
        receipt_processing_service = ReceiptProcessingService()

        first_items = [
            {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
            {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
            {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
            {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
            {
                "shortDescription": "    Klarbrunn 12-PK 12 FL OZ      ",
                "price": "12.00",
            },
        ]
        first_items = [Item(**item) for item in first_items]
        self.assertEqual(receipt_processing_service.every_two_items(first_items), 10)
        self.assertEqual(receipt_processing_service.every_two_items([]), 0)

        second_items = [
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
        ]
        second_items = [Item(**item) for item in second_items]
        self.assertEqual(receipt_processing_service.every_two_items(second_items), 10)

    def test_description_multiple(self):
        receipt_processing_service = ReceiptProcessingService()
        first_items = [
            {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
            {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
            {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
            {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
            {
                "shortDescription": "    Klarbrunn 12-PK 12 FL OZ      ",
                "price": "12.00",
            },
        ]
        first_items = [Item(**item) for item in first_items]
        self.assertEqual(
            receipt_processing_service.description_multiple(first_items), 6
        )

        second_items = [
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
        ]
        second_items = [Item(**item) for item in second_items]
        self.assertEqual(
            receipt_processing_service.description_multiple(second_items), 0
        )

    def test_odd_purchase_date(self):
        receipt_processing_service = ReceiptProcessingService()
        self.assertEqual(receipt_processing_service.odd_purchase_date("2022-01-01"), 6)
        self.assertEqual(receipt_processing_service.odd_purchase_date("2022-01-02"), 0)

    def test_purchase_time(self):
        receipt_processing_service = ReceiptProcessingService()
        start = time(14, 0, 0)
        end = time(16, 0, 0)
        self.assertEqual(
            receipt_processing_service.purchase_time(start, end, "14:01"), 10
        )
        self.assertEqual(
            receipt_processing_service.purchase_time(start, end, "15:33"), 10
        )
        self.assertEqual(
            receipt_processing_service.purchase_time(start, end, "14:00"), 0
        )
        self.assertEqual(
            receipt_processing_service.purchase_time(start, end, "16:00"), 0
        )
        self.assertEqual(
            receipt_processing_service.purchase_time(start, end, "03:43"), 0
        )

    def test_calculate_points(self):

        receipt_processing_service = ReceiptProcessingService()
        first_receipt = {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
                {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
                {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
                {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
                {"shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00"},
            ],
            "total": "35.35",
        }
        first_receipt = Receipt(**first_receipt)
        second_receipt = {
            "retailer": "M&M Corner Market",
            "purchaseDate": "2022-03-20",
            "purchaseTime": "14:33",
            "items": [
                {"shortDescription": "Gatorade", "price": "2.25"},
                {"shortDescription": "Gatorade", "price": "2.25"},
                {"shortDescription": "Gatorade", "price": "2.25"},
                {"shortDescription": "Gatorade", "price": "2.25"},
            ],
            "total": "9.00",
        }
        second_receipt = Receipt(**second_receipt)
        self.assertEqual(receipt_processing_service.calculate_points(first_receipt), 28)
        self.assertEqual(
            receipt_processing_service.calculate_points(second_receipt), 109
        )
