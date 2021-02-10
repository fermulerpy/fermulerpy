import math

import warnings

def get_divisors(n):
    """
    Finds all  divisors of a number
    
    Parameters
    ----------
    n : int
        denotes the natural number of which divisors needs to be calculated
    return : array
        returns an array of divisors of n
        
    """
    if(n<=0):
        raise ValueError(
            "n must be a positive integer"
        )
        
    list1 = []
    
    for i in range(1,n+1):
        if(n%i == 0):
            list1.append(i)
    return list1
    
def divisor_count(n):
    """
    Calculates total number of divisors of given natural number
    
    Parameters
    ----------
    n : int
        denotes the natural number of which divisor count needs to be calculated
    return : int 
        returns an integer specifying number of divisors
        
    """
    if(n<=0):
        raise ValueError(
            "n must be a natural number"
        )
    
    count=0
    
    for i in range(1,n+1):
        if(n%i == 0):
            count += 1
    return count

def divisor_sum(n):
    """
    Calculates the sum of all divisors of n
    
    Parameters
    ----------
    n : int
        denotes the natural number of which sum of divisors needs to be calculated
    return : int
        returns an integer specifying sum of divisors of n
        
    """
    if(n<=0):
        raise ValueError(
            "n must be a positive integer"
        )
    
    sum = 0
    
    for i in range(1,n+1):
        if(n%i == 0):
            sum += i
    return sum
    
