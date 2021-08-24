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
    list2 = []
    for i in range(1,int(math.sqrt(n))+1):
        if(n%i == 0):
            if(i*i == n):
                list1.append(i)
            list1.append(i)
            list2.append(n//i)
    return list1 + list2[::-1]
    
def divisor_count(n):
    """
    Calculates total number of divisors of given natural number i.e., d(n)
    
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
    
    for i in range(1,int(math.sqrt(n))+1):
        if(n%i == 0):
            if(i*i == n):
                count += 1
                continue
            count += 2
    return count

def divisor_sum(n):
    """
    Calculates the sum of all divisors of n i.e., σ(n)
    
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
    
    for i in range(1,int(math.sqrt(n))+1):
        if(n%i == 0):
            if(i*i == n):
                sum += i
                continue
            sum += i
            sum += (n//i)
    return sum
    
def divisor_product(n):
    """
    Calculates the product of the divisors of positive integer n

    Parameters
    ----------
    n : int
        denotes positive integer
    return : int
        returns an integer denoting product of all divisors of n

    """
    if(n<=0 or n!=int(n)):
        raise ValueError(
            "n must be psotive integer"
        )
    divisors_count = divisor_count(n)
    return int(n ** (divisors_count/2))