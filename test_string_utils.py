import pytest
from string_utils import check_string_length

def test_empty_string():
    assert check_string_length("") == "Empty"

def test_short_string():
    assert check_string_length("Hi") == "Short"
    assert check_string_length("Hello") == "Short"

def test_long_string():
    assert check_string_length("Python") == "Long"
    assert check_string_length("Assignment") == "Long"

def test_invalid_input():
    assert check_string_length(123) == "Invalid"