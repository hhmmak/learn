from bankAccount import BankAccount

class RetirementAccount(BankAccount):

    penalty = 1.10

    def __init__(self, is_roth=False, int_rate=1.01, balance=0):
        super().__init__(int_rate, balance)
        self.is_roth = is_roth

    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        super().withdraw(amount)
        return self

    @classmethod
    def update_min_balance(cls, new_rate):
        cls.penalty = new_rate
        return cls