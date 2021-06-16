import pytest

from fermulerpy.elementary import is_pythagorean_triplet, generate_pythagorean_triplet

def test_isPythagorean_triplet1():
    assert is_pythagorean_triplet(3,4,5) == True

def test_isPythagorean_triplet2():
    assert is_pythagorean_triplet(12,5,14) == False

def test_generate_pythagorean_triplet1():
    assert generate_pythagorean_triplet(3,2) == (12,5,13)

def test_generate_pythagorean_triplet2():
    assert generate_pythagorean_triplet(10,5) == (100,75,125)