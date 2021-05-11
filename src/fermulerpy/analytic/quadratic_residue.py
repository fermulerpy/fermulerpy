import math
import warnings

from fermulerpy.elementary import (isPrime, prime_factorization)

def quadratic_residues(p):
    """
    Returns an array of quadratic residues mod p for a given prime p

    Parameters
    ----------
    p : int
        denotes a prime number
    return : array
        returns an array of quadratic residues

    """
    if(p!=int(p) or p<1):
        raise ValueError(
            "p must be positive integer"
        )
    if(isPrime(p)==False):
        raise ValueError(
            "p must be prime number"
        )
    quadratic_residues_array = []
    for i in range(1,int(p/2)+1):
        quadratic_residues_array.append((i*i)%p)
    quadratic_residues_array = sorted(quadratic_residues_array)
    return quadratic_residues_array

def legendre_euler_symbol(n,p):
    """
    Returns 1 if n is quadratic residue mod p else return -1

    Parameters
    ----------
    n : int
        denotes positive integer
    p : int
        denotes prime number
    return : int
        returns 1 if n is quadratic residue mod p else return -1

    """
    if(n!=int(n) or n<1 or p!=int(p) or p<1):
        raise ValueError(
            "n and p must be positive integers"
        )
    if(isPrime(p) == False):
        raise ValueError(
            "p must be prime"
        )
    r = (math.pow(n,(p-1)//2))%p
    r = int(r)
    if(r == 1):
        return r
    else:
        return -1

def jacobi_symbol(n,p):
    """
    Returns jacobi symbol (1 or -1) for given integer n and given prime p

    Parameters
    ----------
    n : int
        denotes positive integer
    p : int
        denotes a prime number
    return : int
        returns 1 or -1

    """
    if(n!=int(n) or n<1 or p!=int(p) or p<1):
        raise ValueError(
            "n and p must be positive integers"
        )
    if(isPrime(p) == False):
        raise ValueError(
            "p must be prime number"
        )

    symbol = 1
    for i in prime_factorization(p):
        symbol = symbol * ( math.pow(legendre_euler_symbol(n,i),prime_factorization(p)[i]) )
    return int(symbol)


