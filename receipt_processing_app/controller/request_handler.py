from typing import Dict

from receipt_processing_app.model.receipt import Receipt
from receipt_processing_app.model.item import Item
from receipt_processing_app.controller.in_memory_database_controller import (
    DataController,
)


class RequestHandler:
    def __init__(self, data_controller: DataController, receipt_processing_service):
        self.data_controller = data_controller
        self.receipt_processing_service = receipt_processing_service

    def process_receipts(self, receipt: Dict) -> str:
        if "items" in receipt:
            receipt["items"] = [Item(**item) for item in receipt["items"]]
        receipt = Receipt(**receipt)
        receipt_id = self.data_controller.create_receipt(receipt)
        return receipt_id

    def get_points(self, receipt_id: str) -> int:
        receipt = self.data_controller.get_receipt(receipt_id)
        total_points = self.receipt_processing_service.calculate_points(receipt)
        return total_points
