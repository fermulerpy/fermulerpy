import math

from fermulerpy.elementary import (isCoprime , isCongruent)
from fermulerpy.constants import factorial

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

def wilson_prime_checker(p):
    """
    Checks if a number is prime according to wilson criteria
    p is a prime if and only if (p - 1)! ≡ -1 (modp)

    Parameters
    ----------
    p : int
        denotes the integer that has to be checked if prime
    return : bool
        returns true if p is prime otherwise false

    """
    if(p<2):
        return False
    return isCongruent(factorial(p-1),-1,p)

def last_digit(a , b):
    """
    Returns last digit of a^b

    Parameters
    ----------
    a : int
        denotes positive integer in a^b
    b : int
        denotes positive integer b in a^b
        
    """
    temp_arr_a = []
    temp_arr_b = []
    while(a>0):
        temp_arr_a.append(a%10)
        a = a//10
    while(b>0):
        temp_arr_b.append(b%10)
        b = b//10
    return LastDigitHelper(temp_arr_a[::-1],temp_arr_b[::-1])

def LastDigitHelper(a, b) : 
    len_a = len(a) 
    len_b = len(b) 

    if (len_a == 1 and len_b == 1 and b[0] == '0' and a[0] == '0') : 
        return 1
  
    if (len_b == 1 and b[0]=='0') : 
        return 1
  
    if (len_a == 1 and a[0] == '0') : 
        return 0
  
    if((Modulo(4, b) == 0)) : 
        exp = 4
    else :  
        exp = Modulo(4, b) 
  
    res = math.pow((int)(a[len_a - 1]), exp) 
  
    return int(res % 10)

def Modulo(a, b) : 
    mod = 0
    for i in range(0, len(b)) : 
        mod = (mod * 10 + (int)(b[i])) % a 
    return mod 

