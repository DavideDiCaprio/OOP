from bank_account import BankAccount

class Bank():
  
  def __init__(self):
    self.client_list = {}

  def print_client_list(self):
    print(self.client_list)

  def open_account(self):
    client_identifier = input('Welcome to the bank, please insert your bank account identifier in the format name_surname:')
    
    if client_identifier in self.client_list:
      print(f'The client {client_identifier} is already registered!')

    first_deposit = float(input('Insert your first deposit:'))
    new_account = BankAccount(first_deposit)
    self.client_list[client_identifier] = new_account

  def withdraw(self):
    client_identifier = input("Enter id:")
    self.client_list[client_identifier].withdraw()

  def deposit(self):
    client_identifier = input("Enter id:")
    self.client_list[client_identifier].deposit()

  def print_balance(self):
    client_identifier = input("Enter id:")
    self.client_list[client_identifier].print_balance()
