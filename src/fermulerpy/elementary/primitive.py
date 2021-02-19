import math

from fermulerpy.elementary import (isCoprime , euler_function , prime_divisors)

def order(a , m):
    """
    Returns order of a modulo m 
    order of a modulo m is the smallest positive integer t such that a^t ≡ 1 (mod m)

    Parameters
    ----------
    a : int
        denotes positive integer a in a^t ≡ 1 (mod m)
    m : int
        denotes positive integer m in a^t ≡ 1 (mod m)
    return : int
        returns least integet t such that a^t ≡ 1 (mod m)

    """
    if(isCoprime(a , m) == False):
        raise ValueError(
            "a and m must be co-prime"
        )
    i = 1
    while True:
        if(((math.pow(a,i)) % m) == 1 ):
            break
        i = i + 1
    return i
  

        
    
