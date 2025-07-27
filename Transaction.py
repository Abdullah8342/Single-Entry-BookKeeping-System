class AddExpense:
    def __init__(self, amount, transaction_type, category, date):
        self.amount = amount
        self.transaction_type = transaction_type
        self.category = category
        self.date = date

    def __str__(self):
        return f"\nDATE: {self.date} \nTRANSACTION TYPE: {self.transaction_type} \nRs: {self.amount} \nDESCRIPTION: ({self.category})"


class AddIncome:
    def __init__(self, amount, transaction_type, date):
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = date

    def __str__(self):
        return f"\nDATE: {self.date} \nTRANSACTION TYPE: {self.transaction_type} \nRs: {self.amount}"
