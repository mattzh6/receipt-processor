from typing import Dict

from model.Receipt import Receipt
from model.Item import Item
from controller.InMemoryDatabaseController import InMemoryDatabaseController
from controller.ReceiptProcessingService import ReceiptProcessingService

class RequestHandler():
    def __init__(self):
        self.inMemoryDatabaseController = InMemoryDatabaseController()
        self.receiptProcessingService = ReceiptProcessingService()

    def processReceipts(self, receipt: Dict) -> str:
        receipt["items"] = [Item(**item) for item in receipt["items"]]
        receipt = Receipt(**receipt)
        receiptId = self.inMemoryDatabaseController.createReceipt(receipt)
        return receiptId

    def getPoints(self, receiptId: str) -> int:
        receipt = self.inMemoryDatabaseController.getReceipt(receiptId)
        totalPoints = self.receiptProcessingService.calculatePoints(receipt)
        return totalPoints
