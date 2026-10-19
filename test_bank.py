
import pytest
from bank import BankAccount, InsufficientFunds


# Step 0.5: Fixture for fresh test data
@pytest.fixture
def account():
    return BankAccount("alice", balance=100)


# Test 1: Deposit increases balance
def test_deposit_increases_balance(account):
    account.deposit(50)
    assert account.balance == 150


# Test 2: Cannot withdraw more than balance
def test_withdraw_more_than_balance_is_refused(account):
    with pytest.raises(InsufficientFunds):
        account.withdraw(500)
    assert account.balance == 100


# Test 3: Each test gets a fresh account
def test_each_test_gets_a_fresh_account(account):
    assert account.balance == 100


# Test 4: Deposit of zero is rejected
def test_deposit_zero_is_refused(account):
    with pytest.raises(ValueError):
        account.deposit(0)
    assert account.balance == 100


# Test 5: Withdraw entire balance
def test_withdraw_entire_balance(account):
    account.withdraw(100)
    assert account.balance == 0


# Test 6: Two consecutive withdrawals
def test_two_withdrawals(account):
    account.withdraw(30)
    account.withdraw(20)
    assert account.balance == 50


# Step 0.6: Floating-point comparison
def test_interest(account):
    account.add_interest(0.10)
    assert account.balance == pytest.approx(110)
