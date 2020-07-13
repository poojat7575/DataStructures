import pytest

from bits import *

def test_check_even():
    assert "even" == check_even_odd(2)

def test_check_odd():
    assert "odd" == check_even_odd(3)

def test_opposites():
    assert False == if_opposite_sign(6, -8)

def test_non_opposites():
    assert True == if_opposite_sign(6, 8)
