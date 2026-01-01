from abc import ABC, abstractmethod

# =======================
# Abstraction
# =======================
class Account(ABC):
    def __init__(self, account_no, customer_name, balance):
        self.account_no = account_no
        self.customer_name = customer_name
        self._balance = balance   # Encapsulation (protected)

    @abstractmethod
    def calculate_interest(self):
        pass

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        print(f"₹{amount} deposited. New balance: ₹{self._balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= amount
        print(f"₹{amount} withdrawn. New balance: ₹{self._balance}")

    def get_balance(self):
        return self._balance


# =======================
# Inheritance + Polymorphism
# =======================
class SavingsAccount(Account):
    def calculate_interest(self):
        interest = self._balance * 0.04
        print(f"Savings Interest: ₹{interest}")
        return interest


class CurrentAccount(Account):
    def calculate_interest(self):
        print("Current Account has no interest")
        return 0


# =======================
# Encapsulation
# =======================
class Customer:
    def __init__(self, name, account):
        self.name = name
        self.__account = account  # private attribute

    def show_balance(self):
        print(f"{self.name}'s Balance: ₹{self.__account.get_balance()}")

    def deposit(self, amount):
        self.__account.deposit(amount)

    def withdraw(self, amount):
        self.__account.withdraw(amount)

    def calculate_interest(self):
        self.__account.calculate_interest()


# =======================
# Application Logic
# =======================
if __name__ == "__main__":
    savings = SavingsAccount(101, "Sankar", 5000)
    current = CurrentAccount(102, "Ravi", 10000)

    customer1 = Customer("Sankar", savings)
    customer2 = Customer("Ravi", current)

    customer1.deposit(2000)
    customer1.calculate_interest()

    customer2.withdraw(3000)
    customer2.calculate_interest()
