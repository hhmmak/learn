from bankAccount import BankAccount

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = [BankAccount()]

    def create_account(self):
        self.account.append(BankAccount())
        return self

    def make_deposit(self, amount, num=0):
        self.account[num].deposit(amount)
        return self
    
    def make_withdrawal(self, amount, num=0):
        self.account[num].withdraw(amount)
        return self

    def display_user_balance(self, num=0):
        print(f"User: {self.name}, Balance of account #{num}: ${self.account[num].balance}")
        if len(self.account) > 1:
            print(f"Total Balance: ${User.total_sum(self.account)}")    #implement staticmethod, print only if user have more than one account
        return self

    def transfer_money(self, other_user, amount, num_self=0, num_other_user=0):
        self.account[num_self].withdraw(amount)
        other_user.account[num_other_user].deposit(amount)
        return self

    @staticmethod   
    def total_sum(account_list):
        sum_num = 0
        for account in account_list:
            sum_num += account.balance
        return sum_num