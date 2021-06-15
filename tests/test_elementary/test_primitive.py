import pytest

from fermulerpy.elementary import order, primitive_root

def test_order1():
    assert order(8,11) == 10

def test_order2():
    assert order(10,11) == 2

def test_primitive_root1():
    assert primitive_root(7) == 3

def test_primitive_root2():
    assert primitive_root(73) == 5