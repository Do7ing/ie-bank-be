from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, country, status and created_at fields are defined correctly
    """
    account = Account('John Doe', '€', 'Spain')
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'
    assert account.country == 'Spain'


def test_account_initial_balance():
    """
    GIVEN a new Account
    WHEN a new Account is created
    THEN check that the initial balance is 0.0
    """
    account = Account('John Doe', '€', 'Spain')
    assert account.balance == 0.0


def test_account_default_status():
    """
    GIVEN a new Account
    WHEN a new Account is created
    THEN check that the default status is 'Active'
    """
    account = Account('John Doe', '€', 'Spain')
    assert account.status == 'Active'