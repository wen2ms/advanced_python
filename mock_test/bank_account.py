import requests


class BankAccount:
    def __init__(self, initial_balance):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdraw amount cannot be negative")
        self.balance -= amount

    def get_intereset_rate(self):
        url = "https://api.exmaple.com/interest_rate"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("rate")
        else:
            raise Exception("Failed to fetch interest rate")