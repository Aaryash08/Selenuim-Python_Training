import pytest
import time

# --- Mock Functional System (The Application Under Test) ---
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        time.sleep(1) # Sleep to simulate network latency for parallel testing demo
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        time.sleep(1)
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

# --- Functional Tests ---

@pytest.fixture
def account():
    return BankAccount(100)

# 1. Write functional tests that test end-to-end behavior
def test_e2e_deposit_flow(account):
    """End-to-End: User opens account, deposits money."""
    new_balance = account.deposit(50)
    assert new_balance == 150

def test_e2e_withdrawal_flow(account):
    """End-to-End: User withdraws money successfully."""
    new_balance = account.withdraw(30)
    assert new_balance == 70

def test_e2e_insufficient_funds(account):
    """End-to-End: User tries to withdraw more than balance."""
    with pytest.raises(ValueError) as excinfo:
        account.withdraw(200)
    assert str(excinfo.value) == "Insufficient funds"

def test_e2e_multiple_transactions(account):
    """End-to-End: Complex transaction history."""
    account.deposit(100)
    account.withdraw(50)
    account.deposit(25)
    assert account.balance == 175

# Adding dummy tests to demonstrate parallel speed-up
@pytest.mark.parametrize("amount", [10, 20, 30, 40, 50])
def test_bulk_processing_simulation(account, amount):
    account.deposit(amount)
    assert account.balance == 100 + amount