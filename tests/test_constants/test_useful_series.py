import pytest

from fermulerpy.constants import ugly_number,ugly_series,fibonacci,fibonacci_series,catalan,catalan_series,factorial,stirling_factorial,bell_number,bell_series,binomialCoef,nCkModp,moser_de_bruijn,moser_de_bruijn_series,golomb,golomb_series

def test_ugly_number1():
    assert ugly_number(1) == 1

def test_ugly_number2():
    assert ugly_number(10) == 12

def test_ugly_number3():
    assert ugly_number(15) == 24
def test_ugly_number4():
    assert ugly_number(150) == 5832

def test_ugly_series1():
    assert ugly_series(2) == [1,2]
def test_ugly_series2():
    assert ugly_series(3) == [1,2,3]
def test_ugly_series3():
    assert ugly_series(7) == [1,2,3,4,5,6,8]
def test_ugly_series4():
    assert ugly_series(10) == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]

def test_fibonacci1():
    assert fibonacci(2) == 1
def test_fibonacci2():
    assert fibonacci(9) == 34
def test_fibonacci3():
    assert fibonacci(23) == 28657
def test_fibonacci4():
    assert fibonacci(154) == 68330027629092351019822533679447

def test_fibonacci_series1():
    assert fibonacci_series(2) == [0,1]
def test_fibonacci_series2():
    assert fibonacci_series(5) == [0,1,1,2,3]
def test_fibonacci_series3():
    assert fibonacci_series(10) == [0,1,1,2,3,5,8,13,21,34]
def test_fibonacci_series4():
    assert fibonacci_series(12) == [0,1,1,2,3,5,8,13,21,34,55,89]

def test_catalan1():
    assert catalan(2) == 2
def test_catalan2():
    assert catalan(5) == 42
def test_catalan3():
    assert catalan(15) == 9694845
def test_catalan4():
    assert catalan(31) == 14544636039226909

def test_catalan_series1():
    assert catalan_series(2) == [1,1]
def test_catalan_series2():
    assert catalan_series(5) == [1,1,2,5,14]
def test_catalan_series3():
    assert catalan_series(9) == [1,1,2,5,14,42,132,429,1430]
def test_catalan_series4():
    assert catalan_series(12) == [1,1,2,5,14,42,132,429,1430,4862,16796,58786]

def test_factorial1():
    assert factorial(5) == 120
def test_factorial2():
    assert factorial(9) == 362880
def test_factorial3():
    assert factorial(8) == 40320
def test_factorial4():
    assert factorial(10) == 3628800

def test_stirling_factorial1():
    assert stirling_factorial(1) == [0.9221370088957891 , 1.00]


def test_bell_number1():
    assert bell_number(1) == 1
def test_bell_number2():
    assert bell_number(8) == 4140
def test_bell_number3():
    assert bell_number(25) == 4638590332229999353
def test_bell_number4():
    assert bell_number(40) == 157450588391204931289324344702531067

def test_bell_series1():
    assert bell_series(2) == [1,1]
def test_bell_series2():
    assert bell_series(3) == [1,1,2]
def test_bell_series3():
    assert bell_series(5) == [1,1,2,5,15]
def test_bell_series4():
    assert bell_series(9) == [1,1,2,5,15,52,203,877,4140]

def test_binomialCoef1():
    assert binomialCoef(3,3) == 1
def test_binomialCoef2():
    assert binomialCoef(5,3) == 10
def test_binomialCoef3():
    assert binomialCoef(5,4) == 5
def test_binomialCoef4():
    assert binomialCoef(5,5) == 1

def test_nCkModp1():
    assert nCkModp(10,2,13) == 6
def test_nCkModp2():
    assert nCkModp(6,2,13) == 2
def test_nCkModp3():
    assert nCkModp(10,6,5) == 0


def test_moser_de_bruijn1():
    assert moser_de_bruijn(1) == 1
def test_moser_de_bruijn2():
    assert moser_de_bruijn(8) == 64
def test_moser_de_bruijn3():
    assert moser_de_bruijn(25) == 321
def test_moser_de_bruijn4():
    assert moser_de_bruijn(40) == 1088


def test_moser_de_bruijn_series1():
    assert moser_de_bruijn_series(2) == [0,1]
def test_moser_de_bruijn_series2():
    assert moser_de_bruijn_series(3) == [0,1,4]
def test_moser_de_bruijn_series3():
    assert moser_de_bruijn_series(5) == [0,1,4,5,16]
def test_moser_de_bruijn_series4():
    assert moser_de_bruijn_series(9) == [0,1,4,5,16,17,20,21,64]


def test_golomb1():
    assert golomb(1) == 1
def test_golomb2():
    assert golomb(8) == 4
def test_golomb3():
    assert golomb(25) == 9
def test_golomb4():
    assert golomb(40) == 12


def test_golomb_series1():
    assert golomb_series(2) == [1,2]
def test_golomb_series2():
    assert golomb_series(3) == [1,2,2]
def test_golomb_series3():
    assert golomb_series(9) == [1,2,2,3,3,4,4,4,5]
def test_golomb_series4():
    assert golomb_series(11) == [1,2,2,3,3,4,4,4,5,5,5]