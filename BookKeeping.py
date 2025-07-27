from Transaction import AddExpense,AddIncome

class Bookkeeping:
    ''' Single Book Keeping Transaction '''
    def __init__(self):
        self.transactions = []

    def add_income(self, amount, date):
        ''' Adding Income in the Account '''
        transaction = AddIncome(amount, 'INCOME (IC)', date)
        self.transactions.append(transaction)

    def add_expense(self, amount, category, date):
        ''' Expense '''
        transaction = AddExpense(amount, 'EXPENSE (EXP)', category, date)
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
        with open(filename, 'w',encoding='utf-8') as file:
            for transaction in self.transactions:
                if transaction.transaction_type == 'INCOME (IC)':
                    file.write(f'{transaction.date},{transaction.transaction_type},{transaction.amount}\n')
                elif transaction.transaction_type == 'EXPENSE (EXP)':
                    file.write(f"{transaction.date},{transaction.transaction_type},{transaction.amount},{transaction.category}\n")

    def load_from_file(self, filename):
        ''' Loarding Data back from the Files '''
        try:
            with open(filename, 'r',encoding='utf-8') as file:
                for line in file:
                    try:
                        date, transaction_type, amount = line.strip().split(',')
                        amount = float(amount)
                        self.transactions.append(AddIncome(amount, transaction_type,date))
                    except:
                        date, transaction_type, amount, category = line.strip().split(',')
                        amount = float(amount)
                        self.transactions.append(AddExpense(amount, transaction_type, category,date))
        except FileNotFoundError:
            print("\nFile not found. Starting with an empty transaction list.")

    def CheckBalance(self):
        total_income,total_expense,net_balance = self.get_summary()
        return net_balance
