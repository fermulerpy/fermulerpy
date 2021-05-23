import math
import warnings

from fermulerpy.elementary import prime_divisors, prime_factorization

def isSum_2_square(n):
    """
    Checks if the given positive integer can be expressed as the sum of squares of two integers

    Parameters
    ----------
    n : int
        denotes postive integer
    return : bool
        returns true if n can be expresses as the sum of two squares otherwise false

    """
    if(n<1 or n!=int(n)):
        raise ValueError(
            "n must be postive integer"
        )
    factorization = prime_factorization(n)
    for i in factorization:
        if(i%4 == 3 and factorization[i]%2 == 1):
            return False
    return True

def sum_2_square(n):
    """
    Finds all representations of n as the sum of two squares

    Parameters
    ----------
    n : int
        denotes positive integer
    return : 2-d array
        returns a 2-d array showing all representations of n as the sum of two squares if possible otherwise returns -1

    """
    if(n<1 or n!=int(n)):
        raise ValueError(
            "n must be postive integer"
        )
    if(isSum_2_square(n) == False):
        return -1
    ans = []
    i = 1
    while(i*i < n):
        req = int(n - (i*i))
        req_root = int(math.sqrt(req))
        if(req_root<i):
            break
        if(req_root*req_root == req):
            t = []
            t.append(i)
            t.append(req_root)
            ans.append(t)
        i = i + 1
    return ans


