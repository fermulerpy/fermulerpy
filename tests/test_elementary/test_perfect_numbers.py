import pytest

from fermulerpy.elementary import isPerfect, generate_euclid_perfect, isAmicable

def test_isPerfect1():
    assert isPerfect(28) == True

def test_isPerfect2():
    assert isPerfect(18) ==False

def test_isPerfect3():
    assert isPerfect(496) == True

def test_generate_euclid_perfect1():
    assert generate_euclid_perfect(2) == 6

def test_generate_euclid_perfect2():
    assert generate_euclid_perfect(7) == 8128

def test_isAmicable1():
    assert isAmicable(220,284) == True

def test_isAmicable2():
    assert isAmicable(6,16) == False