from bank import value
import pytest

def test_value():
    assert value("banana") == "$100"
    assert value("hello") == "$0"
    assert value("happy") == "$20"

def test_value_lowercase():
    assert value("How are you?") == "$100"