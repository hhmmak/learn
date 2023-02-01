class BankAccount:
    
    all_accounts = []

    def __init__(self, int_rate = 1.01, balance = 0):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.amount_valid(self.balance, amount):
            self.balance -= amount
        else:
            print ("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if BankAccount.amount_valid(self.balance, 0):
            self.balance *= self.int_rate
        return self

    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()
        return cls

    @staticmethod
    def amount_valid(amount, minimum):
        if amount >= minimum:
            return True
        else:
            return False