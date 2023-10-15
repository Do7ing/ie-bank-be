from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account('John Doe', '€')
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'
    assert account.country == 'Spain'


def test_create_account_with_initial_balance():
    """
    GIVEN a Account model
    WHEN a new Account is created with an initial balance
    THEN check the initial balance
    """
    account = Account('John Doe', '€', 'Spain')
    assert account.balance == 0.0


def test_account_status():
    """
    GIVEN a new Account
    WHEN a new Account is created
    THEN check the status is active
    """
    account = Account('John Doe', '€', 'Spain')
    assert account.status == 'Active'