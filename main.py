from BookKeeping import Bookkeeping

def main():
    bookkeeping = Bookkeeping()
    bookkeeping.load_from_file('transactions.csv')  # Load existing transactions if any

    while True:
        print("\nWelcome to the Single Entry Bookkeeping System!")
        print("0. Check Balance")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Get Summary")
        print("5. Save and Exit")

        choice = input("\nPlease choose an option: ")
        if choice == '0':
            Total_Balance = bookkeeping.CheckBalance()
            print(f'Total Balance -: {Total_Balance}')
        elif choice == '1':
            amount = float(input("\nEnter income amount: "))
            date = input("\nEnter date (YYYY-MM-DD): ")
            bookkeeping.add_income(amount, date)
        elif choice == '2':
            amount = float(input("\nEnter expense amount: "))
            category = input("\nEnter Category: ")
            date = input("\nEnter date (YYYY-MM-DD): ")
            bookkeeping.add_expense(amount, category, date)
        elif choice == '3':
            bookkeeping.view_transactions()
        elif choice == '4':
            total_income, total_expenses, net_balance = bookkeeping.get_summary()
            print(f"\nTotal Income: Rs-{total_income}")
            print(f"\nTotal Expenses: Rs-{total_expenses}")
            print(f"\nNet Balance: Rs-{net_balance}")
        elif choice == '5':
            bookkeeping.save_to_file('transactions.csv')
            print("\nTransactions saved. Exiting...")
            break
        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main()
