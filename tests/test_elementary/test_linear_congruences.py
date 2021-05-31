import pytest

from fermulerpy.elementary import isSol, sol_count, find_sol

def test_isSol1():
    assert isSol(3,4,5) == True

def test_isSol2():
    assert isSol(4,9,10) == False

def test_sol_count1():
    assert sol_count(6,7,8) == 0

def test_sol_count2():
    assert sol_count(10,200,100) == 10

def test_find_sol1():
    assert find_sol(3,4,5) == [3]

def test_find_sol2():
    assert find_sol(10,200,100) == [-1, 9, 19, 29, 39, 49, 59, 69, 79, 89]