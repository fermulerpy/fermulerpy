import math
import warnings

def divisor_function_avg(n):
    """
    Returns the average order of divisor function for the positive integer n

    Parameters
    ----------
    n : int
        denotes positive integer
    return : float
        return average order of divisor function

    """
    if(n!=int(n) or n<1):
        raise ValueError(
            "n must be positive integer"
        )
    return (math.pow(math.pi,2))*(n/12)

def euler_totient_avg(n):
    """
    Returns the average order of euler totient function for the positive integer n

    Parameters
    ----------
    n : int
        denotes positive integer
    return : float
        return euler totient average

    """
    if(n!=int(n) or n<1):
        raise ValueError(
            "n must be positive integer"
        )
    return (3*n)/(math.pow(math.pi,2))

def mobius_avg(n):
    """
    Returns the average order of mobius function for the positive integer n

    Parameters
    ----------
    n : int
        denotes positive integer
    return : float
        return mobius function average

    """
    if(n!=int(n) or n<1):
        raise ValueError(
            "n must be positive integer"
        )
    return 0.0

def liouville_avg(n):
    """
    Returns the average order of liouville function for the positive integer n

    Parameters
    ----------
    n : int
        denotes positive integer
    return : float
        return liouville function average

    """
    if(n!=int(n) or n<1):
        raise ValueError(
            "n must be positive integer"
        )
    return 1.0