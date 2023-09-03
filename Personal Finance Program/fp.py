import colorama
from colorama import Fore, Style

colorama.init()

transactions = []

def record_income():
    while True:
        amount_str = input("Enter income amount:")
        try:
            amount = float(amount_str)
            if amount < 0:
                print("Invalid amount.")
            else:
                transaction = {"amount": amount, "type": "income"}
                transactions.append(transaction)
                print("Income recorded successfully.")
                break
        except ValueError:
            print("Invalid input.")

def record_expense():
    while True:
        amount_str = input("Enter expense amount:")
        try:
            amount = float(amount_str)
            if amount < 0:
                print("Invalid amount.")
            else:
                break
        except ValueError:
            print("Invalid input.")

    transaction = {"amount": amount, "type": "expense"}
    transactions.append(transaction)
    print("Expense recorded.")

def calculate_total_paid():
    total_paid = sum(transaction["amount"] for transaction in transactions if transaction["type"] == "income")
    return total_paid

def calculate_total_spent():
    total_spent = sum(transaction["amount"] for transaction in transactions if transaction["type"] == "expense")
    return total_spent

def calculate_balance():
    total_paid = calculate_total_paid()
    total_spent = calculate_total_spent()
    balance = total_paid - total_spent
    return balance

def calculate_savings_percentage():
    total_paid = calculate_total_paid()
    total_spent = calculate_total_spent()
    savings_percentage = (total_paid - total_spent) / total_paid * 100
    return savings_percentage

def display_transactions():
    print("Transaction List:")
    for transaction in transactions:
        amount = transaction["amount"]
        if transaction["type"] == "income":
            print(f"  ${Fore.GREEN}{amount:.2f}{Style.RESET_ALL}")
        else:
            print(f"  ${Fore.RED}{amount:.2f}{Style.RESET_ALL}")

def clear_data():
    transactions.clear()
    print("Data cleared.")

def main():
    print("Personal Finance Program")
    print("1. Record Income")
    print("2. Record Expense")
    print("3. Calculate Total Money Paid")
    print("4. Calculate Total Money Spent")
    print("5. Calculate Current Balance")
    print("6. Display Transactions")
    print("7. Calculate Savings Percentage")
    print("8. Clear Data")
    print("Type 'exit' to Exit")

    while True:
        choice = input("Enter choice: ")

        if choice == "1":
            record_income()
        elif choice == "2":
            record_expense()
        elif choice == "3":
            total_paid = calculate_total_paid()
            print("Total money paid:" + Fore.GREEN + f"{total_paid:.2f}" + Style.RESET_ALL)
        elif choice == "4":
            total_spent = calculate_total_spent()
            print("Total money spent:" + Fore.RED + f"{total_spent:.2f}" + Style.RESET_ALL)
        elif choice == "5":
            balance = calculate_balance()
            if balance >= 0:
                print("Money currently in the account: " + Fore.GREEN + f"{balance:.2f}" + Style.RESET_ALL)
            else:
                print("Money currently in the account: " + Fore.RED + f"{balance:.2f}" + Style.RESET_ALL)
        elif choice == "6":
            display_transactions()
        elif choice == "7":
            savings_percentage = calculate_savings_percentage()
            print("Savings Percentage: " + Fore.YELLOW + f"{savings_percentage:.2f}% Saved" + Style.RESET_ALL)
        elif choice == "8":
            clear_data()
        elif choice.lower() == "exit":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()


