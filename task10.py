class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Yangi balans: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Pul yechildi. Yangi balans: {self.balance}")
        else:
            print("Xatolik: yetarli mablag‘ yo‘q.")

# Test
acc = BankAccount("Ali", 500)
acc.deposit(200)
acc.withdraw(100)
acc.withdraw(700)
