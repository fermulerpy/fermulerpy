import warnings
import numpy as np
import math

def ugly_number(n):
    """
    Returns the n'th Ugly number.
    Ugly Numbers are numbers whose only prime factors are 2,3 or 5.

    Parameters
    ----------
    n : int
        represent the position of ugly number
    
    """
    if(n<1):
        raise ValueError(
            "Enter a valid natural number"
        )
    ugly = [0]*n 
    ugly[0] = 1
    i2 = i3 = i5 = 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for l in range(1, n):
        ugly[l] = min(next_multiple_of_2,
                      next_multiple_of_3, 
                      next_multiple_of_5)
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
 
        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
 
        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
    return ugly[-1]

def ugly_series(n):
    """
    Returns n Ugly numbers starting from 1.
    Ugly Numbers are numbers whose only prime factors are 2,3 or 5.

    Parameters
    ----------
    n : int
        represent the count of ugly numbers
    return : array
        return an array of length n
    
    """
    if(n<1):
        raise ValueError(
            "Enter a valid natural number"
        )
    arr = []
    for i in range(0,n):
        arr.append(ugly_number(i+1))
    return arr

def fibonacci(n):
    """
    Returns the n'th fibonacci number starting from 0

    Parameters
    ----------
    n : int
        represent the position of fibonacci number

    """
    a = 0
    b = 1
    if n < 0:
        raise ValueError(
            "Enter a non-negative integer"
        )
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b

def fibonacci_series(n):
    """
    Return a series of n fibonacci numbers

    Parameters
    ----------
    n : int
        represent the count of fibonacci numbers
    return : array
        return an array of length n
    """
    if(n<1):
        raise ValueError(
            "Enter a valid input"
        )
    arr = []
    for i in range(0,n):
        arr.append(fibonacci(i))
    return arr

def catalan(n):
    """
    Returns n'th catalan number

    Parameters
    ----------
    n : int
        represent the position of catalan number starting from zero

    """
    if(n<0):
        raise ValueError(
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

def catalan_series(n):
    """
    Returns first n catalan numbers

    Parameters
    ----------
    n : int
        denotes the count of catalan numbers
    return : array
        returns an array of n catalan numbers

    """
    if(n<1):
        raise ValueError(
            "Enter a positive integer"
        )
    arr = []
    for i in range(0,n):
        arr.append(catalan(i))
    return arr
    
def factorial(n):
    """
    Returns the factorial of n

    Parameters
    ----------
    n : int
        denotes the non-negative integer for which factorial value is needed
    
    """
    if(n<0):
        raise ValueError(
            "Enter a valid non-negative integer"
        )
    
    if(n==0 or n==1):
        return 1
    elif(n==2):
        return 2
    return n*factorial(n-1)

def stirling_factorial(n):
    """
    Returns the upper and lower bounds of Stirling's approximation of a factorial

    Parameters
    ----------
    n : int
        denotes the positive integer for which factorial needs to be approximated
    return : array
        return an array of length 2
        first element denotes lower bound
        second element denotes upper bound

    """
    if(n<0):
        raise ValueError(
            "Enter a valid natural number"
        )
    arr = []
    lower = (math.sqrt(2*math.pi))*(math.pow(n,n+0.5))*(math.pow(math.e,-1*n))
    arr.append(lower)
    upper = (math.e)*(math.pow(n,n+0.5))*(math.pow(math.e,-1*n))
    arr.append(upper)
    return arr

def bell_number(n):
    """
    Returns the n'th bell number

    Parameters
    ----------
    n : int
        denotes the number for which bell number needs to be calculated
    
    """
    if(n<0):
        raise ValueError(
            "Invalid Input"
        )
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1,n+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1,i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    return bell[n][0]

def bell_series(n):
    """
    Returns first n bell numbers

    Parameters
    ----------
    n : int
        denotes the count of bell numbers
    return : array
        return an array of integers
    """
    if(n<1):
        raise ValueError(
            "Invalid Input"
        )
    arr = []
    for i in range(n):
        arr.append(bell_number(i))
    return arr

def binomialCoef(n, k):
    """
    Return the binomial coefficient nCk i.e., coefficient of x^k in (1+x)^n
    
    Parameters
    ----------
    n : int
        denotes n in nCk
    k : int
        denotes k in nCk
    return : int
        return an integer
        
    """
    if(n<k):
        raise TypeError(
            "Value of first argument cannot be smaller than second"
        )
    Coef = [[0 for x in range(k+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                Coef[i][j] = 1
            else:
                Coef[i][j] = Coef[i-1][j-1] + Coef[i-1][j]
 
    return Coef[n][k]

def nCkModp(n, k, p):  
    """
    Returns nCk % p
    
    Parameters
    ----------
    n : int
        denotes n in nCk%p
    k : int
        denotes k in nCk%p
    p : int
        denotes p in nCk%p
    return : int
        returns an integer

    """
    if (k > n- k): 
        k = n - k    
    Coef = [0 for i in range(k + 1)] 
  
    Coef[0] = 1
    for i in range(1, n + 1):  
        for j in range(min(i, k), 0, -1):  
            Coef[j] = (Coef[j] + Coef[j-1]) % p 
    return Coef[k] 

def moser_de_bruijn(n):
    """
    Returns the n'th moser_de_bruijn number

    Parameters
    ----------
    n : int
        denotes the number for which moser_de_bruijn number needs to be calculated
    return : int
        return an integer
    """
    S = [0, 1]
    for i in range(2, n+1):
        if i % 2 == 0:
            S.append(4 * S[int(i / 2)])
        else:
            S.append(4 * S[int(i / 2)] + 1)
    z = S[n]
    return z
    
def moser_de_bruijn_series(n):
    """
    Returns first n moser_de_bruijn numbers

    Parameters
    ----------
    n : int
        denotes the count of moser_de_bruijn numbers
    return : array
        return an array of integers
    """
    arr = []
    for i in range(n):
        arr.append(moser_de_bruijn(i))
    return arr

def golomb(n):
    """
    Returns the n'th golomb number

    Parameters
    ----------
    n : int
        denotes the number for which golomb number needs to be calculated
    return : int
        return an integer
    """
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = 1 + dp[i - dp[dp[i - 1]]] 
    z = dp[n]
    return z

def golomb_series(n):
    """
    Returns first n golomb numbers

    Parameters
    ----------
    n : int
        denotes the count of golomb numbers
    return : array
        return an array of integers
    """
    if(n<1):
        raise ValueError(
            "Invalid Input"
        )
    arr = []
    for i in range(1,n+1):
        arr.append(golomb(i))
    return arr


def newman_conway(n):
    """
    Returns the n'th newman_conway number

    Parameters
    ----------
    n : int
        denotes the number for which newman_conway number needs to be calculated
    return : int
        return an integer
    """
    f = [0, 1, 1]
    for i in range(3, n + 1):
        r = f[f[i-1]]+f[i-f[i-1]]
        f.append(r);
    return f[n]
    
def newman_conway_series(n):
    """
    Returns first n newman_conway numbers

    Parameters
    ----------
    n : int
        denotes the count of newman_conway numbers
    return : array
        return an array of integers
    """
    if(n<1):
        raise ValueError(
            "Invalid Input"
        )
    arr = []
    for i in range(1,n+1):
        arr.append(newman_conway(i))
    return arr

def newman_prime(n):
    """
    Returns the n'th newman_prime number

    Parameters
    ----------
    n : int
        denotes the number for which newman_prime number needs to be calculated
    return : int
        return an integer
    """
    if(n<2): return 1
    a,b=1,1
    for i in range(2,n+1):
        c=2*b+a
        a=b
        b=c
    return b

def newman_prime_series(n):
    """
    Returns first n newman_conway numbers

    Parameters
    ----------
    n : int
        denotes the count of newman_conway numbers
    return : array
        return an array of integers
    """
    arr = []
    for i in range (n):
        arr.append(newman_prime(i))
    return arr

def lobb(n,m):
    """
    Returns the number of ways that n + m open parentheses can be arranged to form the start of a valid sequence of balanced parentheses.

    Parameters
    ----------
    n : int
        denotes n in n+m
    m : int 
        denotes m in n+m
    return : int
        return an integer
    """
    if(n<m):
        raise TypeError(
            "Value of first argument cannot be smaller than second"
        )
    return ((2 * m + 1) * binomialCoef(2 * n, m + n)) // (m + n + 1)

#def lobb_series(n):

def eulerian(n,m):
    """
    Returns the number of permutations of the numbers 1 to n in which exactly m elements are greater than previous element.

    Parameters
    ----------
    n : int
        denotes the total number of elements being considered in the permutation
    m : int 
        denotes the number of elements in the permutation that are greater than the element preceding them.
    return : int
        return an integer
    """
    if(n<m):
        raise TypeError(
            "Value of first argument cannot be smaller than second"
        )
    dp = [0] * (m + 1)
    for i in range(1, n + 1):
        prev = 0
        for j in range(0, m + 1):
            temp = dp[j]
            if i > j:
                if j == 0:
                    dp[j] = 1
                else:
                    dp[j] = ((i - j) * prev) + ((j + 1) * dp[j])
                prev = temp
    return dp[m]

#def eulerian_series(n):

def delannoy(n,m):
    """
    Returns the number of paths from the southwest corner (0, 0) of a rectangular grid to the northeast corner (m, n), using only single steps north, northeast, or east

    Parameters
    ----------
    n : int
        denotes the number of steps you move northward (height of the grid)
    m : int 
        denotes the number of steps you move eastward (width of the grid).
    return : int
        return an integer
    """
    if(n<m):
        raise TypeError(
            "Value of first argument cannot be smaller than second"
        )
    dp = [1] * (n+1)
    for i in range(1, m+1):
        prev = 1
        for j in range(1, n+1):
            temp = dp[j]
            dp[j] = prev + dp[j] + dp[j-1]
            prev = temp
    return dp[n]

#def delannoy_series(n):

def entringer(n,k):
    """
    Returns the number of permutations of {1, 2, …, n + 1}, starting with k + 1, which, after initially falling, alternatively fall then rise.

    Parameters
    ----------
    n : int
        denotes the length of the alternating sequence.
    k : int 
        denotes the the value of the second element.
    return : int
        return an integer
    """
    if(n<k):
        raise TypeError(
            "Value of first argument cannot be smaller than second"
        )
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        curr = [0] * (n + 1)
        for j in range(1, i + 1):
            curr[j] = curr[j - 1] + dp[i - j]
        dp = curr
    return dp[k]

#def entringer_series(n):


def recontres(n,m):
    """
    Returns the number of derangements with k fixed points.

    Parameters
    ----------
    n : int
        denotes the maximum number in the arrangement.
    m : int
        denotes the number of points that needs to be on its original position in the arrangement.
    return : int
        return an integer
    """ 
    if(n<m):
        raise TypeError(
            "Value of first argument cannot be smaller than second"
        )
    w, h = m+1, n+1
    dp= [[0 for x in range(w)] for y in range(h)]
    for i in range(0, n+1) : 
        for j in range(0, m+1) : 
            if (j <= i) :
                if (i == 0 and j == 0) : 
                    dp[i][j] = 1 
                elif (i == 1 and j == 0) : 
                    dp[i][j] = 0
                elif (j == 0) : 
                    dp[i][j] = ((i - 1) * 
                     (dp[i - 1][0] + dp[i - 2][0])) 
                else : 
                    dp[i][j] =  binomialCoef(i,j)* dp[i - j][0] 
                      
    return dp[n][m] 
#def recontres_series(n):
def jacobsthal(n):
    """
    Returns the n'th jacobsthal number

    Parameters
    ----------
    n : int
        denotes the number for which jacobsthal number needs to be calculated
    return : int
        return an integer
    """ 
    prev1, prev2 = 0, 1
    if n == 0:
        return prev1
    if n == 1:
        return prev2
    for i in range(2, n + 1):
        curr = prev2 + 2 * prev1
        prev1, prev2 = prev2, curr
    return curr
    
def jacobsthal_series(n):
    """
    Returns first n jacobsthal numbers

    Parameters
    ----------
    n : int
        denotes the count of jacobsthal numbers
    return : array
        return an array of integers
    """
    arr = []
    for i in range(0,n):
        arr.append(jacobsthal(i))
    return arr
