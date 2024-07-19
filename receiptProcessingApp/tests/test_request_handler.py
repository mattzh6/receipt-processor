import unittest
from receiptProcessingApp.controller.request_handler import RequestHandler


class TestRequestHandler(unittest.TestCase):

    def test_process_receipts(self):
        receipt = {
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
        request_handler = RequestHandler()
        receipt_id = request_handler.process_receipts(receipt)
        total_points = request_handler.get_points(receipt_id)
        self.assertEqual(total_points, 28)

    def test_get_points_with_empty_id(self):
        requestHandler = RequestHandler()
        with self.assertRaises(ValueError):
            requestHandler.get_points("")

    def test_get_points_with_nonexistent_id(self):
        requestHandler = RequestHandler()
        with self.assertRaises(ValueError):
            requestHandler.get_points("this should not exist")