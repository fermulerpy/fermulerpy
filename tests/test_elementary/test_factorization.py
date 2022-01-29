import pytest

from fermulerpy.elementary import isPrime, prime_series, prime, prime_table, SieveOfEratosthenes, prime_divisors, prime_factorization

def test_isPrime1():
    assert isPrime(20) == False

def test_isPrime2():
    assert isPrime(727) == True

def test_isPrime3():
    assert isPrime(7480398387) == False

def test_prime_series1():
    assert prime_series(5) == [2,3,5,7,11]

def test_prime_series2():
    assert prime_series(12) == [2,3,5,7,11,13,17,19,23,29,31,37]

def test_prime1():
    assert prime(1) == 2

def test_prime2():
    assert prime(1000) == 7919

def test_prime3():
    assert prime(6543223) == 114452179

def test_prime_table():
    assert prime_table(8) == [3,7,31,211,2311,30031,510511,9699691]

def test_SieveOfEratosthenes1():
    assert SieveOfEratosthenes(10) == [2,3,5,7]

def test_SieveOfEratosthenes2():
    assert SieveOfEratosthenes(10,20) == [11,13,17,19]

def test_prime_divisors1():
    assert prime_divisors(10) == [2,5]

def test_prime_divisors2():
    assert prime_divisors(100) == [2,5]

def test_prime_factorization1():
    assert prime_factorization(8001) == {3:2, 7:1, 127:1}

def test_prime_factorization2():
    assert prime_factorization(120) == {2:3, 3:1, 5:1}

