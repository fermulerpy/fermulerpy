import pytest

from fermulerpy.elementary import rational_sol, isInteger_sol

def test_rational_sol1():
    sol = rational_sol(5,6,17)
    assert (5*sol[0] + 6*sol[1]) == 17

def test_rational_sol2():
    solutions = rational_sol(5,6,17,4)
    passing = True
    for solution in solutions:
        passing = passing and ((5*solution[0] + 6*solution[1]) == 17)
    assert passing == True

def test_isInteger_sol1():
    assert isInteger_sol(7,17,24) == True

def test_isInteger_sol2():
    assert isInteger_sol(100,34,999) == False