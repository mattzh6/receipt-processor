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
        self.assertEqual(total_round_dollar("0.00"), 50)

if __name__ == "__main__":
    unittest.main()