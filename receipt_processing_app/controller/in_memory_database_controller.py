from receipt_processing_app.controller.data_controller import DataController
from receipt_processing_app.model.receipt import Receipt
import uuid


class InMemoryDatabaseController(DataController):
    def __init__(self):
        self.database = dict()

    def create_receipt(self, receipt: Receipt) -> str:
        receipt_id = str(uuid.uuid4())
        self.database[receipt_id] = receipt
        return receipt_id

    def get_receipt(self, receipt_id: str) -> Receipt:
        if receipt_id in self.database:
            return self.database.get(receipt_id)
        else:
            raise ValueError(
                f"The receipt id given does not exist in the database: {receipt_id}"
            )
