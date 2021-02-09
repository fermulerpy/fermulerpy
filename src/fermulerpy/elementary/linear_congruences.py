import math

import warnings

from fermulerpy.elementary import (gcd , isDivisible , isCoprime)

def isSol(a , b , m):
    """
    Checks if solution exist for the linear congruence equation ax ≡ b (mod m)

    Parameters
    ----------
    a : int
        denotes a in ax ≡ b (mod m)
    b : int
        denotes b in ax ≡ b (mod m)
    m : int
        denotes m in ax ≡ b (mod m)
    return : bool
        returns true if solution exist otherwise false

    """
    return isDivisible(gcd(a , m), b)

def sol_count(a , b , m):
    """
    Returns number of solutions of ax ≡ b (mod m) that are least residue (mod m)

    Parameters
    ----------
    a : int
        denotes a in ax ≡ b (mod m)
    b : int
        denotes b in ax ≡ b (mod m)
    m : int
        denotes m in ax ≡ b (mod m)

    """
    if(isSol(a , b , m) == False):
        return 0
    elif(isCoprime(a , m)):
        return 1
    else:
        return gcd(a , m)

