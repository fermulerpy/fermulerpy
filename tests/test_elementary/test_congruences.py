import pytest

from fermulerpy.elementary import isCongruent, least_residue

def test_isCongruent1():
    assert isCongruent(6,20,7) == True

def test_isCongruent2():
    assert isCongruent(1609,1215,197) == True

def test_isCongruent3():
    assert isCongruent(6,2,7) == False

def test_least_residue1():
    assert least_residue(2,10) == 2

def test_least_residue2():
    assert least_residue(200,17) == 13   
