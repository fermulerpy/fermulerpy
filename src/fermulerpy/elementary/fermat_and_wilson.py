import math

from fermulerpy.elementary import isCoprime

def fermat_prime_checker(p ,a):
    """
    Checks if p is prime using fermat's principle
    If p is prime and gcd(a, p) = 1, then a^(p-1) ≡ 1 (mod p)

    Parameters
    ----------
    p : int
        denotes a natural number that has to be checked for prime
    a : int
        denotes a natural number co-prime with p
    return : bool
        return true if p is prime otherwise false

    """
    if(isCoprime(a , p) == False):
        raise ValueError(
            "a must be co-prime with p"
        )
    
    if(p == 1):
        return False
    return (math.pow(a,p-1) % p) == (1 % p)

    
