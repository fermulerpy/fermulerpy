import pytest 

from fermulerpy.elementary import isTerminate, getPeriod

def test_isTerminate1():
    assert isTerminate(2,20) == True

def test_isTerminate2():
    assert isTerminate(3,1001) == False

def test_getPeriod1():
    assert getPeriod(29) == 28

def test_getPeriod2():
    assert getPeriod(17) == 16