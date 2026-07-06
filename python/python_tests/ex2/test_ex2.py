#Author: Gal Elhiani
#Tester: Tomer Bahar

import pytest
from BankAccount import BankAccount


class TestBankAccount:
    @pytest.fixture
    def account(self):
        return BankAccount(id="1234")
    
    def test_initial_state(self, account):
        assert account.id == "1234"
        assert account.balance == 0
    
    def test_deposit(self, account):
        result = account.deposit(100)
        assert result is True
        assert account.balance == 100

    def test_withdraw(self, account):
        account.deposit(100)
        result = account.withdraw(50)
        assert result is True
        assert account.balance == 50

    def  test_withdraw_over_balance(self, account):
        account.deposit(100)
        result = account.withdraw(500)
        assert result is None
        assert account.balance == 100

