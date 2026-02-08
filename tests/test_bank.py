"""Unit tests for bank.py"""

import pytest

from bank_api.bank import Bank


@pytest.fixture
def bank() -> Bank:
    return Bank()

def test_create_account_raises_error_if_name_blank(bank: Bank):
    # This means: assert an exception is raised during the following block
    with pytest.raises(Exception):
        bank.create_account('')

def test_bank_creates_empty(bank: Bank):
    assert len(bank.accounts) == 0
    assert len(bank.transactions) == 0

def test_can_create_and_get_account(bank: Bank):
    bank.create_account('Test')
    account = bank.get_account('Test')

    assert len(bank.accounts) == 1
    assert account.name == 'Test'

def test_get_account_raises_error_if_no_account_matches(bank: Bank):
    bank.create_account('Name 1')

    # This means: assert an exception is raised during the following block
    with pytest.raises(ValueError):
        bank.get_account('Name 2')

# TODO: Add unit tests for bank.add_funds()

def test_add_funds_can_adds_a_transaction_to_the_correct_account_with_the_correct_amount(
        bank: Bank
    ):
    # ARRANGE
    test_name = "Account 1"
    test_amount = 10
    bank.create_account(test_name)

    # ACT
    bank.add_funds(test_name, test_amount)

    # ASSERT
    assert len(bank.transactions) == 1
    single_transaction = bank.transactions[0]
    assert single_transaction.amount == test_amount
    assert single_transaction.account.name == test_name
