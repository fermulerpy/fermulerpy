import math
import cmath
import warnings

from fermulerpy.elementary import gcd

def fourier_coeff(period,f):
    """
    Returns fourier coefficients of a discrete function.

    Parameters
    ----------
    period : int
        denotes the period of function
    f : array
        denotes the value(integer,floating or complex values) of function f for one period
    return : array(complex)
        returns an array of complex numbers denoting fourier coefficients of function 'f'

    """
    if(period!=int(period) or period<1):
        raise ValueError(
            "period must be positive integer"
        )
    if(len(f)!=period):
        raise ValueError(
            "f must contain exactly period number of values"
        )
    g = []
    for n in range(0,period):
        sum = complex(0,0)
        for m in range(0,period):
            sum = sum + (f[m]*cmath.rect(1,-1*(2*(math.pi)*m*n)/period ) )
        sum = sum/period
        g.append(sum)
    return g

#gauss dirichlet sum (ANT-pg165)

def is_gauss_sum_separable(n,k):
    """
    Returns true if gauss sum is separble for dirichlet characters mod k calculated for positive integer n

    Parameters
    ----------
    n : int
        denotes positive integer for which dirichlet characters are calculated
    k : int
        denotes positive intger mod
    return : bool
        returns true if gauss sum is separable otherwise false

    """
    if(n!=int(n) or k!=int(k) or n<1 or k<1):
        raise ValueError(
            "n and k must be positive integers"
        )
    return gcd(n,k)==1

#conductor of dirichlet character mod k