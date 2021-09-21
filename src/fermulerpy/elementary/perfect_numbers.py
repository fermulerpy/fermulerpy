import math
import warnings

from fermulerpy.elementary import divisor_sum, isPrime

def isPerfect(n):
    """
    Returns true if the given positive integer is perfect

    Parameters
    ----------
    n : int
        denotes positive integer
    return : bool
        returns true if number is perfect otherwise false

    """
    if(n!=int(n) or n<1):
        raise ValueError(
            "n must be positve integer"
        )
    return divisor_sum(n) == 2*n

def generate_euclid_perfect(k):
    """
    Return the perfect number generated from euclid's theorm
    If 2^k - 1 is prime, then (2^k)((2^k)-1) is perfect

    Parameters
    ----------
    k : int
        denotes power of 2 in 2^k -1
    return : int
        returns perfect number

    """
    if(k!=int(k) or k<1):
        raise ValueError(
            "k must be positive integer"
        )
    n = int(math.pow(2,k) - 1)
    if(isPrime(n) == False):
        raise ValueError(
            "invalid k"
        )
    return int((math.pow(2,k-1)) * (math.pow(2,k) - 1))

def isAmicable(n , m):
    """
    Returns true if given pair m and n are amicable

    Parameters
    ----------
    n : int
        denotes positive integer
    m : int
        denotes positive integer
    return : bool
        returns true if given pair is amicable otherwise returns false

    """
    if(n!=int(n) or n<1 or m!=int(m) or m<1):
        raise ValueError(
            "n and m must be positive integer"
        )
    return (divisor_sum(n) == m + n) and (divisor_sum(m) == m+n)


