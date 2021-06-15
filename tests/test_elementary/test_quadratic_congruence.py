import pytest

from fermulerpy.elementary import quad_congruence_solve

def test_quad_congruence_solve1():
    assert quad_congruence_solve(9,11) == [3,8]

def test_quad_congruence_solve2():
    assert quad_congruence_solve(10,5) == -1

def test_quad_congruence_solve3():
    assert quad_congruence_solve(100,11) == [1,10]