import math

from fermulerpy.constants import (catalan , factorial)

def hook_number(n , h_alpha = []):
    """
    Returns value of hook number.
    If λ is a partition of n then the number of standard Young tableaux of shape λ is given by hook number.

    Parameters
    ----------
    n : int
        positive integer
    
    Optional Parameters
    -------------------
    h_alpha : array
        array of integers denoting hook-lengths of the box α in the Young diagram of λ
        If it is empty , then λ is considered as (n,n) .

    """
    if(len(h_alpha) == 0):
        return catalan(n)
    else:
        h_alpha_product = 1
        for i in h_alpha:
            h_alpha_product *= i
        if(factorial(n) % h_alpha_product != 0):
            raise ValueError(
                "Incorrect values of hook-lengths"
            )
        return int(factorial(n) / h_alpha_product)

def macmahon(a , b , c):
    """
    Returns MacMohan formula for the number M(a,b,c).
    It is equal to the number of plane partitions that fit in an (a×b×c) box.

    Parameters
    ----------
    a : int
        denotes length of box
    b : int
        denotes breadth of box
    c : int
        denotes height of box
    return  : int
        returns value of MacMohan formula

    """
    if(a!=int(a) or b!=int(b) or c!=int(c)):
        raise ValueError(
            "dimnsions must be positive integer"
        )
    ans = 1
    for i in range(1,a+1):
        for j in range(1,b+1):
            for k in range(1,c+1):
                ans *= (i+j+k-1)/(i+j+k-2)
    return ans


