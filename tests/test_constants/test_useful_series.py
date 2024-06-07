import pytest

from fermulerpy.constants import ugly_number,ugly_series,fibonacci,fibonacci_series,catalan,catalan_series,factorial,stirling_factorial,bell_number,bell_series,binomialCoef,nCkModp,moser_de_bruijn,moser_de_bruijn_series,golomb,golomb_series,newman_conway,newman_conway_series,newman_prime,newman_prime_series,lobb,eulerian,delannoy,entringer,recontres,jacobsthal,jacobsthal_series
 
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


def test_newman_conway1():
    assert newman_conway(1) == 1
def test_newman_conway2():
    assert newman_conway(9) == 5
def test_newman_conway3():
    assert newman_conway(25) == 15
def test_newman_conway4():
    assert newman_conway(30) == 16


def test_newman_conway_series1():
    assert newman_conway_series(2) == [1,1]
def test_newman_conway_series2():
    assert newman_conway_series(3) == [1,1,2]
def test_newman_conway_series3():
    assert newman_conway_series(11) == [1,1,2,2,3,4,4,4,5,6,7]
def test_newman_conway_series4():
    assert newman_conway_series(15) == [1,1,2,2,3,4,4,4,5,6,7,7,8,8,8]


def test_newman_prime1():
    assert newman_prime(1) == 1
def test_newman_prime2():
    assert newman_prime(8) == 577
def test_newman_prime3():
    assert newman_prime(25) == 1855077841


def test_newman_prime_series1():
    assert newman_prime_series(2) == [1,1]
def test_newman_prime_series2():
    assert newman_prime_series(3) == [1,1,3]
def test_newman_prime_series3():
    assert newman_prime_series(10) == [1,1,3,7,17,41,99,239,577,1393]
def test_newman_prime_series4():
    assert newman_prime_series(15) == [1,1,3,7,17,41,99,239,577,1393,3363,8119,19601,47321,114243]

def test_lobb1():
    assert lobb(3,2) == 5
def test_lobb2():
    assert lobb(5,3) == 35
def test_lobb3():
    assert lobb(10,7) == 950
def test_lobb4():
    assert lobb(20,10) == 574221648


def test_eulerian1():
    assert eulerian(3,1) == 4
def test_eulerian2():
    assert eulerian(5,3) == 26
def test_eulerian3():
    assert eulerian(10,4) == 1310354
def test_eulerian4():
    assert eulerian(30,16) == 42694138146309498709817320643835

def test_delannoy1():
    assert delannoy(3,2) == 25
def test_delannoy2():
    assert delannoy(5,3) == 231
def test_delannoy3():
    assert delannoy(10,9) == 3317445
def test_delannoy4():
    assert delannoy(40,22) == 1391133027965039868369

def test_entringer1():
    assert entringer(6,5) == 61
def test_entringer2():
    assert entringer(5,3) == 14
def test_entringer3():
    assert entringer(10,7) == 46366
def test_entringer4():
    assert entringer(50,18) == 3262201721609207189858026361036976297212416351086313472

def test_recontres1():
    assert recontres(3,1) == 3
def test_recontres2():
    assert recontres(7,2) == 924
def test_recontres3():
    assert recontres(10,4) == 55650
def test_recontres4():
    assert recontres(40,21) == 5874983816812097764953290400

def test_jacobsthal1():
    assert jacobsthal(3) == 3
def test_jacobsthal2():
    assert jacobsthal(10) == 341
def test_jacobsthal3():
    assert jacobsthal(22) == 1398101
def test_jacobsthal4():
    assert jacobsthal(44) == 5864062014805

def test_jacobsthal_series1():
    assert jacobsthal_series(3) == [0,1,1]
def test_jacobsthal_series2():
    assert jacobsthal_series(5) == [0,1,1,3,5]
def test_jacobsthal_series3():
    assert jacobsthal_series(10) == [0,1,1,3,5,11,21,43,85,171]
def test_jacobsthal_series4():
    assert jacobsthal_series(13) == [0,1,1,3,5,11,21,43,85,171,341,683,1365]