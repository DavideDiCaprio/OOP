class BankAccount ():

    def __init__(self,balance=0):
      self.balance = balance  

    def print_balance(self):
      print(f"Current balance is: {self.balance}")

    def withdraw(self):
      self.amount = float(input("Enter amount of operation: "))

      if self.amount > self.balance:
        print("Not enough money!")

      else :
        self.balance -= self.amount

    def deposit(self):
      self.amount = float(input("Enter amount of operation: "))
      self.balance += self.amount
