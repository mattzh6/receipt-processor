class Receipt():
    def __init__(self, retailer, purchase_date, purchase_time, items, total):
        self.retailer = retailer
        self.purchase_date = purchase_date
        self.purchase_time = purchase_time
        self.items = items
        self.total = total

    def get_retailer(self):
        return self.retailer

    def get_purchase_date(self):
        return self.purchase_date

    def get_purchase_time(self):
        return self.purchase_time

    def get_items(self):
        return self.items

    def get_total(self):
        return self.total