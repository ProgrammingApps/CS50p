import pytest
from plate import is_valid

def test_is_valid():
    assert is_valid("") == False

def test_two_letters():
    assert is_valid("SS") == True 

def test_length():
    assert is_valid("S5") == False

def test_no_punct():
    assert is_valid("?!") == False

def test_numbers_at_end():
    assert is_valid("SS44") == True