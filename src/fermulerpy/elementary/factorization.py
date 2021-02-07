import math

import warnings

def isPrime(num):
    """
    Checks if the number is prime

    Parameters
    ----------
    num : int
        denotes a natural number 
    return : bool
        return true if the number is prime otherwise returns false

    """
    if(num < 0):
        raise ValueError(
            "num must be a natural natural"
        )

    if(num <= 1):
        return False
    if(num <= 3):
        return True
    if(num%2 == 0 or num%3==0):
        return False

    i = 5

    while(i*i <= num):
        if(num%i == 0 or num%(i+2) == 0 ):
            return False
        i = i + 6

    return True

#def prime_table
#def sieve....
#def prime_divisors
#def prime_factorizatio
