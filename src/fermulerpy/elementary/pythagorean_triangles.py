import math
import warnings

def is_pythagorean_triplet(a,b,c):
    """
    Checks if a,b and c forms pythagorean triplet i.e., a^2 + b^2 = c^2

    Parameters
    ----------
    a : int
        denotes positive integer a in a^2 + b^2 = c^2
    b : int
        denotes positive integer b in a^2 + b^2 = c^2
    c : int
        denotes positive integer c in a^2 + b^2 = c^2
    return : bool
        returns true if a, b and c forms pythagorean triplet otherwise false

    """

    if(a<1 or a!=int(a) or b<1 or b!=int(b) or c<1 or c!=int(c)):
        raise ValueError(
            "a,b and c are positive integers"
        )
    count = 0
    if(a%2 == 0):
        count += 1
    if(b%2 == 0):
        count += 1
    if(count!=1):
        return False
    if(c%2 == 0):
        return False
    return (a**2) + (b**2) == (c**2)

def generate_pythagorean_triplet(m , n):
    """
    Generates pythagorean triplets from the given two integers

    Parameters
    ----------
    m : int
        denotes positive integer
    n : int
        denotes positive integer
    return : 3 int
        returns three positive integers
        
    """
    if(m<1 or m!=int(m) or n<1 or n!=int(n)):
        raise ValueError(
            "m and n must be positive integers"
        )
    if(m<=n):
        raise ValueError(
            "m must be greater than n"
        )
    a = 2*m*n
    b = (m**2) - (n**2)
    c = (m**2) + (n**2)
    return a,b,c
