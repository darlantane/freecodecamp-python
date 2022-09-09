class Category:
    def __init__(self, description):
        self.description = description
        self.ledger = []
        self.__balance = 0.0
