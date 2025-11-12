from datetime import datetime

class Transaction:
    def __init__(self, type, amount):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.type = type
        self.amount = amount

    def __str__(self):
        return f"{self.date} - {self.type}: ${self.amount:.2f}"

class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("Deposit", amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction("Withdraw", amount))
        else:
            print("Insufficient balance.")

    def print_statement(self):
        print(f"\nAccount Statement for {self.owner}")
        for t in self.transactions:
            print(t)
        print(f"Current Balance: ${self.balance:.2f}")

class ATM:
    def __init__(self):
        self.current_account = None

    def insert_card(self, account):
        self.current_account = account
        print(f"Card inserted for {account.owner}")

    def enter_pin(self, pin):
        print("PIN accepted.")

    def withdraw(self, amount):
        if self.current_account:
            self.current_account.withdraw(amount)

    def deposit(self, amount):
        if self.current_account:
            self.current_account.deposit(amount)

    @property
    def print_statement(self):
        if self.current_account:
            self.current_account.print_statement()


account1 = Account("Kiet", 1000)
atm = ATM()

atm.insert_card(account1)
atm.enter_pin(1234)
atm.deposit(500)
atm.withdraw(300)
atm.withdraw(1500)
atm.print_statement
