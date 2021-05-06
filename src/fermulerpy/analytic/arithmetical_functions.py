import math
import warnings

def mobius(n) :
    """
    Returns the value of mobius function for positive integer n.

    Parameters
    ----------
    n : int
        denotes positive integer for which the value of mobius function is needed
    return : int
        returns the value of mobius function

    """
    if(n<1 or n!=int(n)):
        raise ValueError(
            "n must be positive integer"
        )
    if(n == 1):
        return 1
    if(n == 2):
        return -1
    p = 0
    if (n % 2 == 0) :
     
        n = int(n / 2)
        p = p + 1
        if (n % 2 == 0) :
            return 0

    for i in range(3, int(math.sqrt(n)) + 1) :
        if (n % i == 0) :
         
            n = int(n / i)
            p = p + 1
            if (n % i == 0) :
                return 0
        i = i + 2   
     
    if(p % 2 == 0) :
        return -1
    else :
        return 1

def euler_totient(n) :
    """
    Returns the value for euler totient function for positive integer n

    Parameters
    ----------
    n : int
        denotes positive integer n for which euler totient function value is needed
    return : int
        return euler totient value

    """
    if(n<1 or n!=int(n)):
        raise ValueError(
            "n must be positive integer"
        )
    result = n 
    p = 2
    while p * p<= n :
        if n % p == 0 :
            while n % p == 0 :
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1
    if n > 1 :
        result = result * (1.0 - (1.0 / float(n)))
  
    return int(result)

def  mangoldt(n):
    """
    Returns the value of mangoldt function for positive integer n

    Parameters
    ----------
    n : int
        denotes positive integer n
    return : float
        returns manglodt function value of n

    """
    if(n<1 or n!=int(n)):
        raise ValueError(
            "n must be positive integer"
        )
    d = 2
    while (d<=n):
        if(n%d == 0):
            if (math.log(n,d)-int(math.log(n,d))==0):
                return  math.log(d)
            else:
                return 0
        d += 1
    return 0

def  isValid(n):
    if (n <=0):
        return 0
    elif (n-int(n) != 0):
        return 0
    return 1
def N(n):
    if not  isValid(n):
        return 0
    return n

def  totient_convolution(n):
    """
    Returns the convolution of euler totient function for n

    Parameters
    ----------
    n : int
        denotes posiive integer n
    return : int
        returns the convolution

    """
    if(n<1 or n!=int(n)):
        raise ValueError(
            "n must be positive integer"
        )
    d = 1
    convolution = 0
    while (d<=n):
        if (n%d==0):
            convolution  += euler_totient(d) * N(n/d)
        d += 1
    return  int(convolution)

def  mangoldt_convolution(n):
    """
    Returns the value for mangoldt convulution of n

    Parameters
    ----------
    n : int
        denotes positive integer n for which mangoldt convulution needs to be calculated
    return : int
        returns the value for mangoldt convulution for n

    """
    if(n<1 or n!=int(n)):
        raise ValueError(
            "n must be positive integer"
        )
    d = 1
    convolution = 0
    while (d<=n):
        if (n%d==0):
            convolution  += euler_totient(d) * math.log(n/d)
        d += 1
    return  convolution

def  numberOfFactors(n):
    counter = 0
    while (n>1):
        i = 2
        while (i<=n):
            if (n%i==0):
                n /= i
                counter  += 1
                break
            i += 1
    return  counter

def  liouville(n):
    """
    Returns the value for liouville function for n

    Parameters
    ----------
    n : int
        denotes the positive integer n for which liouville function value is needed
    return : int
        returns the value for liouville function

    """
    if not  isValid(n):
        raise ValueError(
            "n must be positive integr"
        )
    if (n==1):
        return 1
    else:
        return  (-1)** numberOfFactors(n)

#completed