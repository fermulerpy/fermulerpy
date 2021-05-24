import pytest

from fermulerpy.elementary import isDivisible

def test_isDivisible1():
    a = 4
    b = 109
    assert isDivisible(a,b) == False

def test_isDivisible2():
    a = 123
    b = 369
    assert isDivisible(a,b) == True