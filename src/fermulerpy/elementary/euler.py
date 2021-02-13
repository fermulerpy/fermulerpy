import warnings

from fermulerpy.elementary import (prime_divisors , gcd)

def euler_function(n):
    """
    Returns value of euler function for n i.e., φ(n)

    Parameters
    ----------
    n : int
        denotes positive integer greater than 2
    return : int
        returns the value of φ(n)

    """
    if(n < 2):
        raise ValueError(
            "Input must be positive integer greater than 1"
        )
    prime_divisors_arr = prime_divisors(n)

    num = 1
    for i in prime_divisors_arr:
        num *= (i - 1)
    
    den = 1
    for i in prime_divisors_arr:
        den *= i
    
    return int((num * n)/den)

def classes(n):
    """
    Returns different classes for a positive integer n.
    Two integers are in same class only and only if they have same gcd with n.

    Parameters
    ----------
    n : int
        denotes positive integer of which class distribution is neede
    return : dictionary
        key : int
             denotes the gcd values
        value : array
             denotes the elements belonging to same class

    """
    classes_dict = {}
    for i in range(1,n+1):
        if gcd(i,n) in classes_dict:
            classes_dict[gcd(i,n)].append(i)
        else:
            classes_dict[gcd(i,n)] = [i]
    return classes_dict

