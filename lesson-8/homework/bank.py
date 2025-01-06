import json

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }

    @classmethod
    def from_dict(cls, data):
        """Create an Account object from a dictionary."""
        return cls(data["account_number"], data["name"], data["balance"])

class Bank:
    """Manages all bank accounts."""
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        """Create a new account with a unique account number."""
        account_number = str(len(self.accounts) + 1).zfill(6)
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")

    def view_account(self, account_number):
        """View details of an account."""
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Balance: ${account.balance:.2f}")
        else:
            print("Error: Account not found.")

    def deposit(self, account_number, amount):
        """Deposit money into an account."""
        account = self.accounts.get(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                self.save_to_file()
                print(f"Deposited ${amount:.2f}. New Balance: ${account.balance:.2f}")
            else:
                print("Error: Deposit amount must be positive.")
        else:
            print("Error: Account not found.")

    def withdraw(self, account_number, amount):
        """Withdraw money from an account."""
        account = self.accounts.get(account_number)
        if account:
            if amount > 0 and amount <= account.balance:
                account.balance -= amount
                self.save_to_file()
                print(f"Withdrew ${amount:.2f}. New Balance: ${account.balance:.2f}")
            elif amount > account.balance:
                print("Error: Insufficient funds.")
            else:
                print("Error: Withdrawal amount must be positive.")
        else:
            print("Error: Account not found.")

    def save_to_file(self):
        """Save all account details to a file."""
        with open("accounts.txt", "w") as file:
            accounts_data = {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
            json.dump(accounts_data, file)

    def load_from_file(self):
        """Load account details from a file."""
        try:
            with open("accounts.txt", "r") as file:
                accounts_data = json.load(file)
                self.accounts = {acc_num: Account.from_dict(data) for acc_num, data in accounts_data.items()}
        except FileNotFoundError:
            self.accounts = {}

# Command-line interface
def main():
    bank = Bank()
    while True:
        print("\nBank Menu:")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(name, initial_deposit)
        elif choice == "2":
            account_number = input("Enter account number: ")
            bank.view_account(account_number)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)
        elif choice == "4":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)
        elif choice == "5":
            print("Thank you for using the bank application!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
