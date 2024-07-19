import abc
from receipt_processing_app.model.receipt import Receipt


class DataController(abc.ABC):

    @abc.abstractmethod
    def create_receipt(self, receipt: Receipt) -> str:
        pass

    @abc.abstractmethod
    def get_receipt(self, receipt_id: str) -> Receipt:
        pass
