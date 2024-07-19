import abc
from receiptProcessingApp.model.receipt import Receipt

class DataController(abc.ABC):

    @abc.abstractmethod
    def create_receipt(self, receipt: Receipt):
        pass

    @abc.abstractmethod
    def get_receipt(self, receiptId: str):
        pass
