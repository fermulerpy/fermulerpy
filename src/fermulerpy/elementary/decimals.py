import math
import warnings

from fermulerpy.elementary import gcd

def isTerminate(num,den):
    """
    Checks if given fraction's decimal expansion terminates or not

    Parameters
    ----------
    num : int
        denotes numerator of fraction
    den : int
        denotes denominator of fraction
    return : bool
        returns true if decimal expansion terminates otherwise false

    """
    if(num!=int(num) or den!=int(den)):
        raise ValueError(
            "num and den are integers"
        )
    if(den == 0):
        raise ValueError(
            "den cannot be zero"
        )
    num = abs(num)
    den = abs(den)
    if(num == 0):
        return True
    GCD = gcd(num,den)
    num = num/GCD
    den = den/GCD
    while(den > 0):
        if(den%2 == 0):
            den = den//2
        else:
            break
    while(den > 0):
        if(den%5 == 0):
            den = den//5
        else:
            break
    return den==1

def getPeriod(n):
    """
    Returns period of 1/n

    Parameters
    ----------
    n : int
        denotes positive integer
    return : int
        returns an integer denoting period of 1/n

    """
    if(n!=int(n) or n<1):
        raise ValueError(
            "n must be positive integer"
        )
    rem = 1
    for i in range(1,n+2):
        rem = (10 * rem) % n 
    d = rem
    count = 0
    rem = (10 * rem) % n
    count += 1
    while(rem != d):
        rem = (10 * rem) % n
        count += 1
    return count
