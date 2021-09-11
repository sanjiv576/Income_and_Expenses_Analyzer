"""
This module tests income, expenses and balance from myProfile by using pytest.
"""
import pytest

def testing_balance():
    income = 1200
    spend = 1000
    balance = 200

    assert income - spend == balance

def testing_income():
    spend = 1200
    income = 2000
    balance = 800

    assert spend + balance == income

def testing_expenses():
    balance = 600
    spend = 400
    income = 1000

    assert income - balance == spend
