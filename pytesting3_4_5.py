"""
This module tests first name, gender and contact number from registration form by using pytest.
"""
import pytest
@pytest.fixture
def entries_check():
    first_name = "Ram"
    gender = "Male"
    contact = 13874134
    return[first_name, gender, contact]

# skipping this testing as we know by name , Ram is male.
@pytest.mark.skip
def testing_1(entries_check):
    name = "Ram"
    assert entries_check[0] == name

def testing_2(entries_check):
    gender_type = "Male"
    assert entries_check[1] == gender_type

def testing_3(entries_check):
    # giving incorrect contact number
    contact_num = 12345678
    assert entries_check[2] == contact_num