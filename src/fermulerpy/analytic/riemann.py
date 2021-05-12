import mpmath as mp
import warnings

def zeta_function(s,a = 1,derivative = 0):
    """
    Returns the value for hurwitz-zeta function at s

    Parameters
    ----------
    s : int, float, complex
        denotes the value for which zeta function needs to be calculated
    a : int, float, complex, tuple
        denotes constant a in hurwitz zeta function
        default value is 1
        can be rational also like p/q, input must be a tuple (p,q) for this case, also p and q must be integers
    derivative : int
        denotes the n'th derivative
        default value is 0
    return : float, complex
        returns tha value of zeta function or its derivative

    """
    if(derivative != int(derivative) or derivative <1):
        raise ValueError(
            " derivative must be positive integer"
        ) 
    return mp.zeta(s,a,derivative)

def altzeta_function(s):
    """
    Returns tha value for dirichlet eta function (also alternating zeta function) at s.

    Parameters
    ----------
    s : int, float, complex
        denotes the value for which alternating zeta function needs to be calculated
    return : float, complex
        returns the value of alternating zeta function  

    """
    return mp.altzeta(s)

