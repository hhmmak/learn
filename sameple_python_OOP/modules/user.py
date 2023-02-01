from bankAccount import BankAccount
from retirementAccount import RetirementAccount

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {"regular" : [BankAccount()]}

    def create_account(self, account_type="regular"):
        if account_type not in self.account:
            self.account[account_type] = []

        if account_type == "regular":
            self.account[account_type].append(BankAccount())
        elif account_type == "retirement":
            self.account[account_type].append(RetirementAccount())
        return self

    def make_deposit(self, amount, num=0, account_type="regular"):
        self.account[account_type][num].deposit(amount)
        return self
    
    def make_withdrawal(self, amount, num=0, account_type="regular"):
        self.account[account_type][num].withdraw(amount)
        return self

    def display_user_balance(self, num=0, account_type="regular"):
        print(f"User: {self.name}, Balance of account #{num}: ${self.account[account_type][num].balance}")
        print(f"Total Balance: ${User.total_sum(self.account)}")
        return self

    def transfer_money(self, other_user, amount, num_self=0, num_other_user=0):
        self.account["regular"][num_self].withdraw(amount)
        other_user.account["regular"][num_other_user].deposit(amount)
        return self

    @staticmethod   
    def total_sum(account_list):
        sum_num = 0
        for account_type in account_list:
            for account in account_list[account_type]:
                sum_num += account.balance
        return sum_num