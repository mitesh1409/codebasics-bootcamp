# Throw/raise exceptions example

class InsufficientFunds(Exception):
    pass

balance = 0

def deposit(amount):
    global balance

    if amount <= 0:
        raise ValueError("Deposit amount must be positive")

    balance += amount

def withdraw(amount):
    global balance

    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")

    if amount > balance:
        raise InsufficientFunds("Withdrawal amount can't be more than the balance")

    balance -= amount

deposit(10)
deposit(10)
deposit(10)
# deposit(0)
print(balance)

# withdraw(-5)
withdraw(25)
withdraw(25)
print(balance)
