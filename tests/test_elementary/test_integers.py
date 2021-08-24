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
    assert lcm(a,b) == 100 and lcm(500,100) == 500

def test_lcm2():
    a = 343
    b = 280
    assert lcm(a,b) == 13720

def test_lcm3():
    a = 234516789234023485693020129
    b = 176892058718950472893785940
    assert lcm(a,b) == 41484157651764614525905399263631111992263435437186260

def test_lcm4():
    a = 36594652830916364940473625749407
    b = 448507083624364748494746353648484939
    assert lcm(a,b) == 443593541011902763984944550799004089258248037004507648321189937329

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