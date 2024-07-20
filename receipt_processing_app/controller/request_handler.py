from typing import Dict

from receipt_processing_app.model.receipt import Receipt
from receipt_processing_app.model.item import Item
from receipt_processing_app.controller.in_memory_database_controller import (
    DataController,
)
from receipt_processing_app.controller.receipt_processing_service import (
    ReceiptProcessingService,
)


class RequestHandler:
    def __init__(
        self,
        data_controller: DataController,
        receipt_processing_service: ReceiptProcessingService,
    ):
        self.data_controller = data_controller
        self.receipt_processing_service = receipt_processing_service

    def process_receipts(self, receipt: Dict) -> str:
        """
        Creates a Receipt object, stores that receipt in the database and returns a unique id for that receipt.
        :param receipt: A Dict object representing the receipt.
        :return: A string representing the unique id associated with the receipt.
        """
        if "items" in receipt:
            receipt["items"] = [Item(**item) for item in receipt["items"]]
        receipt = Receipt(**receipt)
        receipt_id = self.data_controller.create_receipt(receipt)
        return receipt_id

    def get_points(self, receipt_id: str) -> int:
        """
        Takes a receipt id and return the reward points calculated from that receipt.
        :param receipt_id: A string representing a receipt's unique id
        :return: A integer representing the reward points for a receipt.
        """
        receipt = self.data_controller.get_receipt(receipt_id)
        total_points = self.receipt_processing_service.calculate_points(receipt)
        return total_points
