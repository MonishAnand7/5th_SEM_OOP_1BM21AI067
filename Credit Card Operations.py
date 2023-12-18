class CreditCard:
    def __init__(self, limit):
        self.__limit = limit
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal of ${amount} processed. Remaining balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit of ${amount} processed. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def display(self):
        print(f"Credit Card Information:")
        print(f"  Limit: ${self.__limit}")
        print(f"  Current Balance: ${self.__balance}")

credit_card = CreditCard(limit=5000)

print("Current Balance:", credit_card.get_balance())

credit_card.deposit(1000)
credit_card.withdraw(500)
credit_card.withdraw(2000)
credit_card.deposit(3000)

credit_card.display()
