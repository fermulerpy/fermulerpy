import pytest

from fermulerpy.elementary import fermat_prime_checker, wilson_prime_checker, last_digit

def test_fermat_prime_checker1():
    assert fermat_prime_checker(89,2) == True

def test_fermat_prime_checker2():
    assert fermat_prime_checker(10,3) == False

def test_wilson_prime_checker1():
    assert wilson_prime_checker(10) == False

def test_wilson_prime_checker2():
    assert wilson_prime_checker(13) == True

def test_last_digit1():
    assert last_digit(5,120) == 5

def test_last_digit2():
    assert last_digit(13,8) == 1