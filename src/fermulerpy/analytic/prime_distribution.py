import math
import warnings

from fermulerpy.analytic import mangoldt

def pi_asymptotic(n):
    """
    Returns the value of asymptotic function for the distribution of prime numbers.

    Parameters
    ----------
    n : int
        denotes positive integer
    return : int
        returns the value of asymptotic function for n

    """
    if(n!=int(n) or n<1):
        raise ValueError(
            "n must be positive integer"
        )
    
    return int(n/(math.log(n)))

def chebyshev_chix(n):
    """
    Returns the value of chebyshev's function chix for positive integer n

    Parameters
    ----------
    n : int
        denotes positive integer
    return : float
        returns the value for chebyshev function

    """
    if(n!=int(n) or n<1):
        raise ValueError(
            "n must be positive integer"
        )
    value = 0.0
    for i in range(1,n+1):
        value = value + mangoldt(i)
    return value

def chebyshev_chix_asymptotic(n):
    """
    Returns the asymptotic value of chebyshev chi(x) function

    Parameters
    ----------
    n : int
        denotes positive integer
    return : int
        returns the asymptotic estimate of chebyshev chi(x) function for n

    """
    if(n!=int(n) or n<1):
        raise ValueError(
            "n must be positive integer"
        )
    return int(n)
    