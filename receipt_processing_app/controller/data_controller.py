import abc
from receipt_processing_app.model.receipt import Receipt


class DataController(abc.ABC):

    @abc.abstractmethod
    def create_receipt(self, receipt: Receipt) -> str:
        """
        This method stores a receipt in the database and returns the associated receipt id.
        :param receipt: A Receipt object.
        :return: A string that represents the receipt id associated with the Receipt object.
        """
        pass

    @abc.abstractmethod
    def get_receipt(self, receipt_id: str) -> Receipt:
        """
        Get a Receipt from the database from a given receipt id.
        :param receipt_id: A string that represents a receipt id associated to a specific Receipt object in the database.
        :return: A Receipt object.
        """
        pass
