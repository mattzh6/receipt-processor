from typing import Dict

from receiptProcessingApp.model.receipt import Receipt
from receiptProcessingApp.model.item import Item
from receiptProcessingApp.controller.in_memory_database_controller import InMemoryDatabaseController
from receiptProcessingApp.controller.receipt_processing_service import ReceiptProcessingService

class RequestHandler():
    def __init__(self):
        self.in_memory_database_controller = InMemoryDatabaseController()
        self.receipt_processing_service = ReceiptProcessingService()

    def process_receipts(self, receipt: Dict) -> str:
        receipt["items"] = [Item(**item) for item in receipt["items"]]
        receipt = Receipt(**receipt)
        receipt_id = self.in_memory_database_controller.create_receipt(receipt)
        return receipt_id

    def get_points(self, receiptId: str) -> int:
        receipt = self.in_memory_database_controller.get_receipt(receiptId)
        total_points = self.receipt_processing_service.calculate_points(receipt)
        return total_points
