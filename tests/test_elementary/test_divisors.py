import pytest

from fermulerpy.elementary import get_divisors, divisor_count, divisor_sum

def test_get_divisors1():
    assert get_divisors(10) == [1,2,5,10]

def test_get_divisors2():
    num = 1000
    divisors = []
    for i in range(1,num+1):
        if(num % i == 0):
            divisors.append(i)
    assert get_divisors(num) == divisors

def test_divisor_count1():
    assert divisor_count(10) == 4

def test_divisor_count1():
    num = 1000
    cnt = 0
    for i in range(1,num+1):
        if(num%i == 0):
            cnt = cnt + 1
    assert divisor_count(num) == cnt

def test_divisor_sum1():
    assert divisor_sum(10) == 18

def test_divisor_sum2():
    num = 1000
    sum_divisors = 0
    for i in range(1,num+1):
        if(num % i == 0):
            sum_divisors += i
    assert divisor_sum(num) == sum_divisors
