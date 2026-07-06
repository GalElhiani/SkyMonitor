#Author: Gal Elhiani
#Tester: Tomer Bahar

from BankAccount import BankAccount
import unittest


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(id="Alison Burgers")
        self.account.balance = 100
    
    def test_withdraw(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)


    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_withdraw_over_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)
    
    def test_boundary(self):
        self.account.withdraw(100)
        self.assertEqual(self.account.balance, 0)