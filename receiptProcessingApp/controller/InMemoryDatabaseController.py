from receiptProcessingApp.controller.DataController import DataController
from receiptProcessingApp.model.Receipt import Receipt
import uuid

class InMemoryDatabaseController(DataController):
    def __init__(self):
        self.database = dict()


    def createReceipt(self, receipt: Receipt) -> str:
        receiptId = str(uuid.uuid4())
        self.database[receiptId] = receipt
        return receiptId

    def getReceipt(self, receiptId: str) -> Receipt:
        if receiptId in self.database:
            return self.database.get(receiptId)
        else:
            raise ValueError(f"The receipt id given does not exist in the database: {receiptId}")