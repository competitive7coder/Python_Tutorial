# ❌ Without encapsulation (BAD)
from logging import raiseExceptions


class Product:
    def __init__(self, price):
        self.price = price

p = Product(100)
p.price = -500   # ❌ allowed
# 💥 Bug created. No protection.

# ✅ With encapsulation (GOOD)
class Product:
    def __init__(self, price):
        self._price = price   # internal

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Invalid price")
        self._price = value


p = Product(100)
print("Price before update", p.price)
p.price = 200     # ✅
# p.price = -50     # ❌ ValueError
print("Price after update", p.price)


# ✅ EXAMPLE 2: READ-ONLY ID (identity protection)
class User:
    def __init__(self, user_id):
        self._id = user_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value <= 0:
            raise ValueError("ID cant be negative")
        self._id = value



u = User(10)

print(u.id)   # ✅ allowed
# u.id = 20
# u.id = -10
# print(u.id)   ValueError: ID cant be negative

# ✅ EXAMPLE 3: BANK ACCOUNT (state protection)
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    @balance.setter
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

acc = BankAccount(1000)
print(acc.balance)
acc.deposit = 500   # uses property here ✅
print(f"After deposite the current balance is: ", acc.balance)
acc.withdraw(200)    # ✅
print(f"After withdraw the current balance is: ", acc.balance)

# acc.withdraw(5000)   # ❌
# ❌ No one can do:

acc._balance = -999999   # BAD PRACTICE
# ✔ State always valid



# EXAMPLE 6: PROTECTED METHOD (internal workflow)
class Service:
    def process(self):
        self._validate()
        print("Processing done")

    def _validate(self):
        print("Internal validation done")

s = Service()
s.process()     # ✅ correct
# s._validate()   # ⚠️ works, but DON’T