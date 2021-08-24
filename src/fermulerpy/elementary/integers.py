import math

import warnings

def isDivisible(a,b):
    """
    Check if a divides b

    Parameters
    ----------
    a : int
        denotes a in a|b
    b : int
        denotes b in a|b
    return : bool
        return true if a divides b
        return false if a doesn't divide b

    """
    if(a==0 or b%a != 0):
        return False
    else:
        return True

def gcd(a,b):
    """
    Calculates Greatest Common Divisor of a and b

    Parameters
    ----------
    a : int
        non-negative integer of which gcd is needed
    b : int 
        non-negative integer of which gcd is needed
    return : int
        returns integer gcd value

    """
    return math.gcd(a,b)

def lcm(a,b):
    """
    Calculates least common multiple of a and b

    Parameters
    ----------
    a : int
        non-negative integer of which lcm is needed
    b : int 
        non-negative integer of which lcm is needed
    return : int
        returns integer lcm value
    
    """
    product = a*b
    return product // gcd(a,b)

def division_algo_coeff(a,b):
    """
    Calculates coefficients q and r in a = bq + r according to division algo

    Parameters
    ----------
    a : int
        denotes a in a = bq + r
    b : int 
        denotes b in a = bq + r
    return : two int
        return two integers
        first one refers to q (quotient)
        second one refers to r (remainder)

    """
    if(b == 0):
        raise TypeError(
            "Cannot divide by zero"
        )
    quotient = int(a/b)
    remainder = a%b
    return quotient , remainder

def isCoprime(a,b):
    """
    Checks if two given integers are co-prime

    Parameters
    ----------
    a : int
        denotes first integer
    b : int
        denotes second integer
    return : bool
        returns true if given two integers are co-prime, otherwise returns false

    """
    return gcd(a,b)==1

def euclidean_algo(a,b):
    """
    Prints every step of The Euclidean Algorithm

    Parameters
    ----------
    a : int
        denotes the first integer
    b : int
        denotes the second integer
    return : Null
        Doesn't return anything. Rather it prints every step of euclidean algorithm

    """
    if(b==0):
        raise ZeroDivisionError(
            "b cannot be zero"
        )
    while(a%b != 0 ):
        print(a ,"=",int(a/b),"*",b,"+",a%b)
        temp  = a
        a=b
        b=temp%b
    print(a ,"=",int(a/b),"*",b)

