import pytest

from fermulerpy.elementary import isDivisible, gcd, lcm, division_algo_coeff, isCoprime

def test_isDivisible1():
    a = 4
    b = 109
    assert isDivisible(a,b) == False

def test_isDivisible2():
    a = 123
    b = 369
    assert isDivisible(a,b) == True

def test_gcd1():
    a = 2
    b = 100
    assert gcd(a,b) == 2

def test_gcd2():
    a = 343
    b = 280
    assert gcd(a,b) == 7

def test_lcm1():
    a = 2
    b = 100
    assert lcm(a,b) == 100

def test_lcm2():
    a = 343
    b = 280
    assert lcm(a,b) == 13720

def test_division_algo_coeff1():
    a = 280
    b = 63
    q, r = division_algo_coeff(280,63)
    assert q == 4 and r == 28

def test_isCoprime1():
    a = 343
    b = 10000
    assert isCoprime(a,b) == True

def test_isCoprime2():
    a = 100
    b = 77895345
    assert isCoprime(a,b) == False