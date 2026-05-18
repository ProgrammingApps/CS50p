from twttr import shorten
import pytest



def test_shorten():
    assert shorten("Hello") == "Hll"
    assert shorten("134534") == "134534"
    assert shorten("EOIae") == ""

