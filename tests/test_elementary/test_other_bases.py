import pytest

from fermulerpy.elementary import deci_to_base, base_to_deci

def test_deci_to_base1():
    assert deci_to_base(10,2) == "1010"

def test_deci_to_base2():
    assert deci_to_base(100,6) == "244"

def test_base_to_deci1():
    assert base_to_deci("244",6) == 100

def test_base_to_deci2():
    assert base_to_deci("54AB",16) == 21675