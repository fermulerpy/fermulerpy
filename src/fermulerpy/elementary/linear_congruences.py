import math

import warnings

from fermulerpy.elementary import (gcd , isDivisible , isCoprime)

def isSol(a , b , m):
    """
    Checks if solution exist for the linear congruence equation ax ≡ b (mod m)

    Parameters
    ----------
    a : int
        denotes a in ax ≡ b (mod m)
    b : int
        denotes b in ax ≡ b (mod m)
    m : int
        denotes m in ax ≡ b (mod m)
    return : bool
        returns true if solution exist otherwise false

    """
    return isDivisible(gcd(a , m), b)

def sol_count(a , b , m):
    """
    Returns number of solutions of ax ≡ b (mod m) that are least residue (mod m)

    Parameters
    ----------
    a : int
        denotes a in ax ≡ b (mod m)
    b : int
        denotes b in ax ≡ b (mod m)
    m : int
        denotes m in ax ≡ b (mod m)

    """
    if(isSol(a , b , m) == False):
        return 0
    elif(isCoprime(a , m)):
        return 1
    else:
        return gcd(a , m)

def find_sol(a , b , m):
    """
    Finds all solutions of equation ax ≡ b (mod m)

    Parameters
    ----------
    a : int
        denotes a in ax ≡ b (mod m)
    b : int
        denotes b in ax ≡ b (mod m)
    m : int
        denotes m in ax ≡ b (mod m)

    """
    solutions  = []

    if(isSol(a , b , m) == False):
        return solutions

    elif(sol_count(a , b , m) == 1):
        for i in range(1,m):
            if(((a*i) %m) == (b%m)):
                solutions.append(i)
                return solutions
                
    else:
        temp_gcd = gcd(a,m)
        a = a//temp_gcd
        b = b//temp_gcd
        m = m//temp_gcd
        temp_ans = -1
        for i in range(1,m):
            if(((a*i) %m) == (b%m)):
                temp_ans = i
                break
        for i in range(temp_gcd):
            solutions.append(temp_ans + (i*m))
        return solutions
    

