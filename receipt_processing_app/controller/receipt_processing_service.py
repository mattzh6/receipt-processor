from datetime import datetime
from datetime import time
from decimal import Decimal
from receipt_processing_app.model.receipt import Receipt
from receipt_processing_app.model.item import Item
from typing import List


class ReceiptProcessingService:

    def alphanumeric_count(self, retailer_name: str) -> int:
        """
        Counts the number of alphanumeric characters and returns points associated to that number.
        :param retailer_name: A string that represents the retailer name.
        :return: An integer that represents the points calculated from alphanumeric characters.
        """
        total = 0
        for char in retailer_name:
            if (97 <= ord(char) <= 122) or (65 <= ord(char) <= 90):
                total += 1
        return total

    def total_round_dollar(self, total: str) -> int:
        """
        Calculates if the total dollar amount is a round dollar and rewards points based on that criteria.
        :param total: A string representing the dollar amount.
        :return: An integer that represents the points calculated from round dollar amount with no cents.
        """
        total = Decimal(total)
        # Assume that total being 0 would not reward any points even if it is a round dollar amount with no cents
        if total == 0:
            return 0
        rounded_total = total * 100
        if rounded_total % 100:
            return 0
        return 50

    def total_multiple(self, total: str) -> int:
        """
        Calculates if the total dollar amount is a multiple of .25 cents and rewards points based on that.
        :param total: A string representing the dollar amount.
        :return: A integer that represents the points calculated from a multiple of .25 cents.
        """
        total = Decimal(total)
        # Assume that a total being 0 doesn't reward any points
        if total == 0:
            return 0
        if not total % Decimal(0.25):
            return 25
        return 0

    def every_two_items(self, items: List[Item]) -> int:
        """
        Calculates the number of pairs of items in a list and returns points based on the number of pairs.
        :param items: A list of Item objects.
        :return: An integer that represents the points calculated from number of pairs of items.
        """
        if not items:
            return 0
        total_pairs = len(items) // 2
        return total_pairs * 5

    def description_multiple(self, items: List[Item]) -> int:
        """
        Calculates reward points from a list of items with trimmed descriptions that has a length that is a multiple of 3.
        :param items: A list of Items.
        :return: An integer representing the points from the items with trimmed descriptions that had lengths that were multiples of 3.
        """
        total = 0
        for item in items:
            trimmed_description = item.short_description.strip()
            if not len(trimmed_description) % 3:
                price = Decimal(item.price) * Decimal(0.2)
                rounded_price = round(price + Decimal(0.5))
                total += rounded_price
        return total

    def odd_purchase_date(self, purchase_date: str) -> int:
        """
        Calculates reward points based on if the purchase date day is odd.
        :param purchase_date: A string representing a purchase date.
        :return: An integer representing the points rewarded from purchase dates with odd days.
        """
        purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
        if purchase_date.day % 2:
            return 6
        return 0

    def purchase_time(self, start: time, end: time, purchase_time: str) -> int:
        """
        Calculates reward points based on if the purchase time is within a specific start and end range.
        :param start: A time object representing the start of the time range.
        :param end: A time object representing the end of the time range.
        :param purchase_time: A string representing the time of the purchase.
        :return: An integer representing the points rewarded from having a purchase day within a specific range.
        """
        purchase_time = datetime.strptime(purchase_time, "%H:%M")
        if start < purchase_time.time() < end:
            return 10
        return 0

    def calculate_points(self, receipt: Receipt) -> int:
        """
        Calculate all the reward points from multiple rules.
        :param receipt: A Receipt object.
        :return: An integer representing the total reward points from a given receipt.
        """
        START = time(14, 0, 0)
        END = time(16, 0, 0)
        rewards_points = 0
        rewards_points += self.alphanumeric_count(receipt.retailer)
        rewards_points += self.total_round_dollar(receipt.total)
        rewards_points += self.total_multiple(receipt.total)
        rewards_points += self.every_two_items(receipt.items)
        rewards_points += self.description_multiple(receipt.items)
        rewards_points += self.odd_purchase_date(receipt.purchase_date)
        rewards_points += self.purchase_time(START, END, receipt.purchase_time)
        return rewards_points
