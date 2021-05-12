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

def gamma_function(s):
    """
    Returns tha value for gamma function at s

    Parameters
    ----------
    s : int, float, complex
        denotes the value for which gamma function needs to be calculated
    return : float, complex
        returns the value for gamma function

    """
    return mp.gamma(s)

def bernoulli_num(n):
    """
    Returns n'th bernoulli number

    Parameters
    ----------
    n : int
        positive integer value
    return : float
        returns bernoulli number

    """
    return mp.bernoulli(n)
