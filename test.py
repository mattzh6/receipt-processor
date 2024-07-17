import unittest
from rules import *

class TestRulesMethods(unittest.TestCase):
    
    def test_alphanumeric_count(self):
        self.assertEqual(alphanumeric_count("Target"), 6)
        self.assertEqual(alphanumeric_count("M&M Corner Market"), 14)
        self.assertEqual(alphanumeric_count("?><$#  #\n\t"), 0)
        self.assertEqual(alphanumeric_count(""), 0)

    def test_total_round_dollar(self):
        self.assertEqual(total_round_dollar("9.00"), 50)
        self.assertEqual(total_round_dollar("4.50"), 0)
        self.assertEqual(total_round_dollar("0.00"), 0)

    def test_total_multiple(self):
        self.assertEqual(total_multiple("35.35"), 0)
        self.assertEqual(total_multiple("0.00"), 0)
        self.assertEqual(total_multiple("9.00"), 25)
        self.assertEqual(total_multiple("156.25"), 25)
        self.assertEqual(total_multiple("56.50"), 25)
        self.assertEqual(total_multiple("6.75"), 25)

    def test_every_two_items(self):
        self.assertEqual(every_two_items([
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
        ]), 10)
        self.assertEqual(every_two_items([]), 0)
        self.assertEqual(every_two_items([
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
        ]), 10)

    def test_description_multiple(self):
        self.assertEqual(description_multiple([
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
              "shortDescription": "Klarbrunn 12-PK 12 FL OZ",
              "price": "12.00"
            }
          ]), 6)
        self.assertEqual(description_multiple([
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
      ]), 0)


if __name__ == "__main__":
    unittest.main()