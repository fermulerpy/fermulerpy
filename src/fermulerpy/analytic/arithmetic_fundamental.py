import math

import warnings

from fermulerpy.elementary import gcd as gcd_helper

def gcd(*args):
    """
    Returns Greatest Common Divisor of Multiple Integers

    Parameters
    ----------
    *args : tuple
        tuple of integers
    return : int
        returns an integer gcd
    """
    if(len(args)<2):
        raise ValueError(
            "Invalid Number Of Arguments"
        )
    elif(len(args) >= 2):
        ans = gcd_helper(args[0],args[1])
        if(len(args) == 2):
            return ans
        else:
            for i in range(2,len(args)):
                ans  = gcd_helper(ans,args[i])
            return ans


