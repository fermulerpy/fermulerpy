import math
import warnings

def euler_pentagonal_num(n):
    """
    Returns n'th euler pentagonal number (1-indexed)

    Parameters
    ----------
    n : int
        denotes positive integer
    return : int
        returns n'th euler pentagonal number

    """
    if(n!=int(n) or n<1):
        raise ValueError(
            "n must be positive integer"
        )
    return int(((3*n*n) - n)/2)

def checkRecursive(num, rem_num, next_int, n, ans=0):
 
    if (rem_num == 0):
        ans += 1
 
    r = int(num**(1 / n))
 
    for i in range(next_int + 1, r + 1):
        a = rem_num - int(i**n)
        if a >= 0:
            ans += checkRecursive(num, rem_num - int(i**n), i, n, 0)
    return ans
 
 
def partition_unique(x, n=1):
    """
    Returns the number of ways in which a positive integer x can be expressed as sum of n-th power of unique natural numbers

    Parameters
    ----------
    x : int
        denotes positive integer
    n : int
        denotes positive integer
        default value is 1
    return : int
        returns the total ways of partition

    """
    if(n!=int(n) or n<1 or x!=int(x) or x<1):
        raise ValueError(
            "n and x must be positive integers"
        )
    return checkRecursive(x, x, 0, n)


