from fuel import convert, gauge
import pytest 

def test_convert():
    assert convert("1/2") == 50

def test_gauge():
    assert gauge(100) == "F"
