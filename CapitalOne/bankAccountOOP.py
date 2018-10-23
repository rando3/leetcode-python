class BankAccount:
    def __init__(self, balance=0.00):
        self._balance = balance

    def deposit(self, amount):
        """make a deposit"""
        self._balance += amount

    def withdraw(self, amount):
        """make a withdrawal"""
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount

    @property
    def balance(self):
        """check the balance"""
        return self._balance


class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print 'Sorry, minimum balance must be maintained.'
        else:
            BankAccount.withdraw(self, amount)