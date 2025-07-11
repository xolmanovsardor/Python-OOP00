class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def show_balance(self):
        print(f"{self.owner} balans: {self.balance}")

# Test
a1 = BankAccount("Ali", 500)
a2 = BankAccount("Malika", 800)
a3 = BankAccount("John", 300)

a1.deposit(200)
a2.withdraw(100)
a3.deposit(500)

a1.show_balance()
a2.show_balance()
a3.show_balance()
