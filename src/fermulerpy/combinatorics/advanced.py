import math

from fermulerpy.constants import (catalan , factorial , binomialCoef)



def lovasz(n , k):
    """
    Returns chromatic number value for Kneser Graph.
    Kneser graph is the graph on k-subsets of {1,…,n} with two subsets made adjacent when they are disjoint.

    Parameters
    ----------
    n : int
        denotes n in universal set {1,2,3,....n}
    k : int
        denotes number of subsets
    return : int
        returns integer value denotic chromatic number

    """
    if(n!=int(n) or k!=int(k)):
        raise ValueError(
            "n and k must be integer"
        )
    
    return n - (2*k) + 2


