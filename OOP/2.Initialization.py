class BankAccount:
    def __init__(self, account_number, owner, balance = 0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'${amount} has add to your account')
        else:
            print('The amount must be greater than 0')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Cannot withdraw because the balance do not have enough money!!')
        elif amount <= 0:
            print('Withdraw must be greater than 0')
        else:
            self.balance -= amount
            print(f'${amount} have been withdrawn')

    def get_balance(self):
        print(f'Account ID: {self.account_number}')
        print(f'Account owner: {self.owner}')
        print(f'Account balance: {self.balance}')

acc1 = BankAccount("123456", "Nguyen Duong Gia Thuan")

acc1.deposit(500)
acc1.deposit(200)

acc1.withdraw(100)
acc1.withdraw(800)

acc1.get_balance()
