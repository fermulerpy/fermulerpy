import warnings

import numpy as np

def ugly_number(n):
    """
    Returns the n'th Ugly number.
    Ugly Numbers are numbers whose only prime factors are 2,3 or 5.

    Parameters
    ----------
    n : int
        represent the position of ugly number
    
    """
    if(n<1):
        raise NotImplementedError(
            "Enter a valid natural number"
        )
    ugly = [0]*n 
    ugly[0] = 1
    i2 = i3 = i5 = 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for l in range(1, n):
        ugly[l] = min(next_multiple_of_2,
                      next_multiple_of_3, 
                      next_multiple_of_5)
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
 
        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
 
        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
    return ugly[-1]

def ugly_series(n):
    """
    Returns n Ugly numbers starting from 1.
    Ugly Numbers are numbers whose only prime factors are 2,3 or 5.

    Parameters
    ----------
    n : int
        represent the count of ugly numbers
    return : array
        return an array of length n
    
    """
    if(n<1):
        raise NotImplementedError(
            "Enter a valid natural number"
        )
    arr = []
    for i in range(0,n):
        arr.append(ugly_number(i+1))
    return arr

def fibonacci(n):
    """
    Returns the n'th fibonacci number starting from 0

    Parameters
    ----------
    n : int
        represent the position of fibonacci number

    """
    a = 0
    b = 1
    if n < 0:
        raise NotImplementedError(
            "Enter a non-negative integer"
        )
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b

def fibonacci_series(n):
    """
    Return a series of n fibonacci numbers

    Parameters
    ----------
    n : int
        represent the count of fibonacci numbers
    return : array
        return an array of length n
    """
    if(n<1):
        raise NotImplementedError(
            "Enter a valid input"
        )
    arr = []
    for i in range(0,n):
        arr.append(fibonacci(i))
    return arr

