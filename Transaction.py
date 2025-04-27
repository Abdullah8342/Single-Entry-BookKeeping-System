class Transaction:
    def __init__(self, amount, transaction_type, description, date):
        self.amount = amount
        self.transaction_type = transaction_type  # 'income' or 'expense'
        self.description = description
        self.date = date

    def __str__(self):
        return f"\nDATE: {self.date} \nTRANSACTION TYPE: {self.transaction_type} \nRs: {self.amount} \nDESCRIPTION: ({self.description})"
