class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")

    def display(self):
        print("\nAccount Details")
        print("Account Number:", self.account_number)
        print("Name:", self.name)
        print("Account Type:", self.account_type)
        print("Balance:", self.balance)
account = BankAccount(101, "John", "Savings", 5000)
account.display()
account.deposit(2000)
account.withdraw(1000)
account.display()
