import pytest

from fermulerpy.elementary import isSum_2_square, sum_2_square

def test_isSum_2_square1():
    assert isSum_2_square(25) == True

def test_isSum_2_square2():
    assert isSum_2_square(530) == True

def test_isSum_2_square3():
    assert isSum_2_square(3) == False

def test_sum_2_square1():
    assert sum_2_square(80) == [[4,8]]