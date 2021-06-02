import pytest

from fermulerpy.elementary import euler_function, classes

def test_euler_function1():
    assert euler_function(10) == 4

def test_euler_function2():
    assert euler_function(9) == 6

def test_classes1():
    assert classes(10) == {1: [1, 3, 7, 9], 2: [2, 4, 6, 8], 5: [5], 10: [10]}

def test_classes2():
    assert classes(15) == {1: [1, 2, 4, 7, 8, 11, 13, 14], 3: [3, 6, 9, 12], 5: [5, 10], 15: [15]}


    