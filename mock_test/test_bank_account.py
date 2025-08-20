import unittest
from unittest.mock import patch
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.account = BankAccount(100)

    def tearDown(self):
        print("tearDown")

    def test_create_account(self):
        self.assertIsInstance(self.account, BankAccount)

        with self.assertRaises(ValueError):
            BankAccount(-100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(
            self.account.balance, 150, msg="Blance should be 100 + 50 after deposit"
        )

        with self.assertRaises(ValueError, msg="Negative deposit should raise ValueError"):
            self.account.deposit(-50)

    def test_withdraw(self):
        self.account.withdraw(50)
        self.assertEqual(
            self.account.balance, 50, msg="Blance should be 100 - 50 after withdraw"
        )

        with self.assertRaises(ValueError, msg="Negative withdraw should raise ValueError"):
            self.account.withdraw(-50)

    def test_get_interest_rate(self):
        with patch("bank_account.requests.get") as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {"rate": 0.5}
            interest_rate = self.account.get_intereset_rate()
            self.assertEqual(interest_rate, 0.5)

if __name__ == "__main__":
    unittest.main()
