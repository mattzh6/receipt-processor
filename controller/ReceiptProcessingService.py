from datetime import datetime
from datetime import time
from model import Receipt

class ReceiptProcessingService():

    def alphanumeric_count(self, retailer_name):
        total = 0
        for char in retailer_name:
            if (97 <= ord(char) <= 122) or (65 <= ord(char) <= 90):
                total += 1
        return total

    def total_round_dollar(self, total):
        total = float(total)
        # Assume that total being 0 would not reward any points even if it is a round dollar amount with no cents
        if total == 0:
            return 0
        roundedTotal = total * 100 // 100
        if roundedTotal != 0 and total % roundedTotal:
            return 0
        return 50

    def total_multiple(self, total):
        total = float(total)
        # Assume that a total being 0 doesn't reward any points
        if total == 0:
            return 0
        if not total % 0.25:
            return 25
        return 0

    def every_two_items(self, items):
        if not items:
            return 0
        total_pairs = len(items) // 2
        return total_pairs * 5

    def description_multiple(self, items):
        total = 0
        for item in items:
            trimmed_description = item["shortDescription"].strip()
            if not len(trimmed_description) % 3:
                price = float(item["price"]) * 0.2
                rounded_price = round(price + 0.5)
                total += rounded_price
        return total

    def odd_purchase_date(self, purchase_date):
        purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
        if purchase_date.day % 2:
            return 6
        return 0

    def purchase_time(self, start, end, purchase_time):
        purchase_time = datetime.strptime(purchase_time, "%H:%M")
        if (start < purchase_time.time() < end):
            return 10
        return 0

    def calculate_points(self, receipt: Receipt) -> int:
        START = time(14, 0, 0)
        END = time(16, 0, 0)
        rewards_points = 0
        rewards_points += self.alphanumeric_count(receipt.get_retailer())
        rewards_points += self.total_round_dollar(receipt.get_total())
        rewards_points += self.total_multiple(receipt.get_total())
        rewards_points += self.every_two_items(receipt.get_items())
        rewards_points += self.description_multiple(receipt.get_items())
        rewards_points += self.odd_purchase_date(receipt.get_purchase_date())
        rewards_points += self.purchase_time(START, END, receipt.get_purchase_time())
        return rewards_points