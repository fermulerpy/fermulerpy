import math
import warnings
 
def factorial(n):
    """
    Returns the value of factorial of non-negative integer n

    Parameters
    ----------
    n : int
        denotes non-negative integer
    return : int
        returns integer value denoting factorial of n

    """
    if(n<0):
        raise ValueError(
            "n must be non-negative integer"
        )

    if(n == 0 or n == 1):
        return 1
    
    return n*factorial(n-1)

def permutation(n, k , repetition = False): 
    """
    Returns permutation coefficient.
    It is used to represent the number of ways to obtain an ordered subset having k elements from a set of n elements.

    Parameters 
    ----------
    n : int
        non-negative integer
    k : int
        non-negative integer
    return : int
        returns integer value denoting permutation coefficient
    
    Optional Parameters
    -------------------
    repetition : bool
        By default , it is false.
        If set to 'True' , then it denotes that repetition is allowed

    """
    if(n < k):
        raise ValueError(
            "n cannot be less than k"
        )
    
    if(n<0 or k<0):
        raise ValueError(
            "n and k must be non-negative"
        )
    if(repetition == False):
        Fn = 1
    
        for i in range(1, n + 1): 
            Fn *= i 
            if (i == n - k): 
                Fk = Fn 
    
        coeff = Fn // Fk 
        return coeff 
    else:
        return int(math.pow(n , k))

def combination(n, k , repetition = False): 
    """
    Returns binomial coefficient.

    Parameters 
    ----------
    n : int
        non-negative integer
    k : int
        non-negative integer
    return : int
        returns integer value denoting binomial coefficient
    
    Optional Parameters
    -------------------
    repetition : bool
        By default , it is false.
        If set to 'True' , then it denotes that repetition is allowed

    """
    if(n < 0 or k<0):
        raise ValueError(
            "n and k must be non-negative"
        )

    if(repetition == False):
        if(k > n - k): 
            k = n - k 
        
        res = 1
        
        for i in range(k): 
            res = res * (n - i) 
            res = res / (i + 1) 
        return int(res) 
    else:
        return combination(n + k - 1 , k)

def circular_permutation(n):
    """
    Returns number of circular permutation of n

    Parameters
    ----------
    n : int
        non-negative integer
    return : int
        returns an integer denoting circular permutations of n

    """
    if(n<1):
        raise ValueError(
            "n must be integer greater than 1"
        )
    return factorial(n-1)

def catalan(n):
    """
    Returns n'th catalan number

    Parameters
    ----------
    n : int
        represent the position of catalan number starting from zero

    """
    if(n<0):
        raise NotImplementedError(
            "Enter a valid natural number"
        )
    if(n==0 or n==1):
        return 1
    catalan = [0]*(n+1)
    catalan[0] = 1
    catalan[1] = 1
    for i in range(2,n+1):
        for j in range(i):
            catalan[i] += catalan[j]*catalan[i-j-1]
    return catalan[n]