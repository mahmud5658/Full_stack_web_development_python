class BankingSystem:
    def __init__(self, holder_name, initial_balance):
        self.holder_name = holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit Successful! Updated Balance: ${self.balance:.2f}")
        else:
            print("Error: Deposit amount must be greater than 0.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient balance.")
        elif amount <= 0:
            print("Error: Withdrawal amount must be greater than 0.")
        else:
            self.balance -= amount
            print(f"Withdrawal Successful! Updated Balance: ${self.balance:.2f}")
    def get_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")


def main():
    print("Welcome to the Banking Management System")
    name = input("Enter the account holder's name: ")
    try:
        initial_balance = float(input("Enter the initial balance: "))
    except ValueError:
        print("Invalid input. Initial balance set to $1000.00 by default.")
        initial_balance = 1000.0

    system = BankingSystem(holder_name=name, initial_balance=initial_balance)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Inquiry")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            try:
                amount = float(input("Enter amount to deposit: "))
                system.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == 2:
            try:
                amount = float(input("Enter amount to withdraw: "))
                system.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == 3:
            system.get_balance()
        elif choice == 4:
            print("Thank you for using the Banking Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")


if __name__ == "__main__":
    main()
