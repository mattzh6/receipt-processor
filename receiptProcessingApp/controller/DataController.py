import abc
from receiptProcessingApp.model.Receipt import Receipt

class DataController(abc.ABC):

    @abc.abstractmethod
    def createReceipt(self, receipt: Receipt):
        pass

    @abc.abstractmethod
    def getReceipt(self, receiptId: str):
        pass
