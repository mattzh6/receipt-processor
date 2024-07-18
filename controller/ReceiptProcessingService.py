from datetime import datetime
from datetime import time
from decimal import Decimal
from model.Receipt import Receipt
from model.Item import Item
from typing import List

class ReceiptProcessingService():

    def alphanumeric_count(self, retailerName: str):
        total = 0
        for char in retailerName:
            if (97 <= ord(char) <= 122) or (65 <= ord(char) <= 90):
                total += 1
        return total

    def total_round_dollar(self, total: str):
        total = Decimal(total)
        # Assume that total being 0 would not reward any points even if it is a round dollar amount with no cents
        if total == 0:
            return 0
        roundedTotal = total * 100 // 100
        if roundedTotal != 0 and total % roundedTotal:
            return 0
        return 50

    def total_multiple(self, total: str):
        total = Decimal(total)
        # Assume that a total being 0 doesn't reward any points
        if total == 0:
            return 0
        if not total % Decimal(0.25):
            return 25
        return 0

    def every_two_items(self, items: List[Item]):
        if not items:
            return 0
        total_pairs = len(items) // 2
        return total_pairs * 5

    def description_multiple(self, items: List[Item]):
        total = 0
        for item in items:
            trimmed_description = item.getShortDescription.strip()
            if not len(trimmed_description) % 3:
                price = Decimal(item.getPrice) * Decimal(0.2)
                rounded_price = round(price + Decimal(0.5))
                total += rounded_price
        return total

    def odd_purchase_date(self, purchaseDate: str):
        purchaseDate = datetime.strptime(purchaseDate, "%Y-%m-%d")
        if purchaseDate.day % 2:
            return 6
        return 0

    def purchase_time(self, start: time, end: time, purchaseTime: str):
        purchaseTime = datetime.strptime(purchaseTime, "%H:%M")
        if (start < purchaseTime.time() < end):
            return 10
        return 0

    def calculate_points(self, receipt: Receipt) -> int:
        START = time(14, 0, 0)
        END = time(16, 0, 0)
        rewards_points = 0
        rewards_points += self.alphanumeric_count(receipt.getRetailer)
        rewards_points += self.total_round_dollar(receipt.getTotal)
        rewards_points += self.total_multiple(receipt.getTotal)
        rewards_points += self.every_two_items(receipt.getItems)
        rewards_points += self.description_multiple(receipt.getItems)
        rewards_points += self.odd_purchase_date(receipt.getPurchaseDate)
        rewards_points += self.purchase_time(START, END, receipt.getPurchaseTime)
        return rewards_points