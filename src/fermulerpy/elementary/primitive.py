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
  
def primitive_root(p):
    """
    Returns the smallest primitive root of positive integer p

    Parameters
    ----------
    p : int
        denotes positive integer
    return : int
        returns integer primitive root if exist otherwise returns -1
        
    """
    if(p<1 or p!=int(p)):
        raise ValueError(
            "n must be positive integer"
        )
    fact = []
    phi = euler_function(p)
    n = phi
    i = 2
    while(i*i <= n):
        if(n%i == 0):
            fact.append(i)
            while(n%i == 0):
                n /= i
        i = i + 1
    if(n > 1):
        fact.append(n)
    res = 2
    while(res<=p):
        ok = True
        size = len(fact)
        i = 0
        while(i<size and ok):
            r = pow(res, int(phi / fact[i]), p)
            ok &= (r != 1)
            i = i+1
        if(ok):
            return res
        res = res + 1
    return -1


    

        
    
