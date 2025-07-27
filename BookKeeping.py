from Transaction import Transaction

class Bookkeeping:
    ''' Single Book Keeping Transaction '''
    def __init__(self):
        self.transactions = []

    def add_income(self, amount, description, date):
        ''' Adding Income in the Account '''
        transaction = Transaction(amount, 'INCOME (IC)', description, date)
        self.transactions.append(transaction)

    def add_expense(self, amount, description, date):
        ''' Expense '''
        transaction = Transaction(amount, 'EXPENSE (EXP)', description, date)
        self.transactions.append(transaction)

    def view_transactions(self):
        ''' Transaction Details '''
        for transaction in self.transactions:
            print(transaction)

    def get_summary(self):
        ''' Account Summary '''
        total_income = sum(t.amount for t in self.transactions if t.transaction_type == 'INCOME (IC)')
        total_expenses = sum(t.amount for t in self.transactions if t.transaction_type == 'EXPENSE (EXP)')
        net_balance = total_income - total_expenses
        return total_income, total_expenses, net_balance

    def save_to_file(self, filename):
        ''' Saving Records into the File for Latter Use '''
        with open(filename, 'w') as file:
            for transaction in self.transactions:
                file.write(f"{transaction.date},{transaction.transaction_type},{transaction.amount},{transaction.description}\n")

    def load_from_file(self, filename):
        ''' Loarding Data back from the Files '''
        try:
            with open(filename, 'r') as file:
                for line in file:
                    date, transaction_type, amount, description = line.strip().split(',')
                    amount = float(amount)
                    self.transactions.append(Transaction(amount, transaction_type, description, date))
        except FileNotFoundError:
            print("\nFile not found. Starting with an empty transaction list.")
