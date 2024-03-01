import json
import datetime
import random
class Account:
    def __init__(self, number_account, holder_account, initial_balance=0, status="Active"):
        self.number_account = number_account
        self.holder_account = holder_account
        self.balance = initial_balance
        self.status = status
    # def number_account(self):
    #     self.number_account() = random.randint(10000,20000)
    # روش دلخواه من
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount} to account {self.number_account}. New balance: {self.balance}"
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount} from account {self.number_account}. New balance: {self.balance}"
        else:
            return "Insufficient funds."
    def balance_get(self):
        return f"Current balance of account {self.number_account}: {self.balance}"
    def status_check(self):
        return f"Account {self.number_account} is {self.status}"

class Transaction:
    def __init__(self, id_transaction, type_transaction, amount):
        self.id_transaction = id_transaction
        self.type_transaction = type_transaction
        self.amount = amount
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # sare in dahanam srvice shod

    def details_transaction_get(self):
        return f"Transaction {self.id_transaction}: {self.type_transaction} {self.amount} at {self.timestamp}"
class Bank:
    def __init__(self):
        self.accounts = []
    def account_create(self, holder_account, initial_balance=0, status="Active"):
        account_number = len(self.accounts) + 1
        new_account = Account(account_number, holder_account, initial_balance, status)
        self.accounts.append(new_account)
        return f"Account {account_number} created for {holder_account}."
    def close_account(self, account_number):
        for account in self.accounts:
            if account.number_account == account_number:
                self.accounts.remove(account)
                return f"Account {account_number} closed successfully."
        return f"Account {account_number} not found."
    def perform_transaction(self, account_number, transaction_type, amount):
        for account in self.accounts:
            if account.number_account == account_number:
                if transaction_type == "deposit":
                    return account.deposit(amount)
                elif transaction_type == "withdraw":
                    return account.withdraw(amount)
                else:
                    return "Invalid transaction type."
        return f"Account {account_number} not found."

    #mahal neveshte shodan etelaat hesab karbari
    def report_generate(self):
        report = {"accounts": []}
        for account in self.accounts:
            account_info = {
                "account_number": account.number_account,
                "holder": account.holder_account,
                "balance": account.balance,
                "status": account.status
            }
            report["accounts"].append(account_info)
        return json.dumps(report, indent=2)
bank = Bank()
print(bank.account_create("asghar farhadi", initial_balance=1000))
print(bank.account_create("ahmadi nezhad", initial_balance=500))
print(bank.perform_transaction(1, "deposit", 200))
print(bank.perform_transaction(2, "withdraw", 100))
print(bank.report_generate())

#csv balad naboodam.
