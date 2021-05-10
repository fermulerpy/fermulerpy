import math
import warnings

from fermulerpy.elementary import (gcd, isPrime)

#dirichlet character table generator : to be done

def if_infinite_prime_AP(a,d):
    """
    Returns true if there exist infinte number of prime numbers in the arithmetic progression having first term as 'a' and common difference 'd'

    Parameters
    ----------
    a : int
        integer denoting first term of AP
    d : int
        integer denoting common difference of Ap
    return : bool
        return true if there exist infinte primes in AP otherwise false

    """
    if(a!=int(a) or d!=int(d)):
        raise ValueError(
            "a and d must be integer"
        )
    
    return gcd(a,d) == 1

def prime_count_AP(n,a,d):
    """
    Returns the count of prime numbers less than or equal to n in AP defined by first term as 'a' and common difference 'd'

    Parameters
    ----------
    n : int
        upper bound for prime numbers
    a : int
        first term of AP
    d : int
        common difference of AP
    return : int
        returns the count of prime numbers

    """
    if(n!=int(n) or a!=int(a) or d!=int(d)):
        raise ValueError(
            "n , a and d are integers"
        )
    if(if_infinite_prime_AP(a,d) == False):
        raise ValueError(
            "a and d must be coprime"
        )
    x = a
    count = 0
    while(x <= n):
        if(isPrime(x) == True):
            count = count + 1
        x = x + d
    return count

