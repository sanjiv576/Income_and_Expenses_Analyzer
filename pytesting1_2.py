"""
This module tests username and password by using pytest.
"""
import pytest
# ("admin", "admin") is already created username and password but ("admin", "admin123") is not created yet.

@pytest.mark.parametrize("username, password",[("admin", "admin"), ("admin", "admin123")])
def test_method(username, password):
    assert username == password

