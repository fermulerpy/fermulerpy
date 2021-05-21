import math
import warnings

def deci_to_base(n, base):
    """
    Converts given decimal number into required 'base'

    Parameters
    ----------
    n : int
        denotes positive integer
    base : int
        denotes positive integer representing requuired base
    return : string
        returns a string of required converted number

    """
    if(n!=int(n) or n<1 or base!=int(base) or base<1):
        raise ValueError(
            "n and base must be positive integers"
        )

    index = 0 
    res = ""
    while (n > 0):
        res+= reVal(n % base)
        n = int(n / base)
    res = res[::-1]
 
    return res

def reVal(n):
 
    if (n >= 0 and n <= 9):
        return chr(n+ ord('0'))
    else:
        return chr(n - 10 + ord('A'))

def base_to_deci(str,base):
    """
    Converts a number given in some base to its decimal equivalent

    Parameters
    ----------
    str : string
        denotes a string of number in some base
    base : int
        denotes postive integral base
    return : int
        returns decimal number

    """
    llen = len(str)
    power = 1 
    num = 0    
    for i in range(llen - 1, -1, -1):
        if val(str[i]) >= base:
            raise ValueError(
                "invalid number"
            )
            return -1
        num += val(str[i]) * power
        power = power * base
    return num

def val(c):
    if c >= '0' and c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

 