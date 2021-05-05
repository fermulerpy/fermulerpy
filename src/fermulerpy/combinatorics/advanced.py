import math

from fermulerpy.constants import (catalan , factorial , binomialCoef)

def hook_number(n , h_alpha = []):
    """
    Returns value of hook number.
    If λ is a partition of n then the number of standard Young tableaux of shape λ is given by hook number.

    Parameters
    ----------
    n : int
        positive integer
    
    Optional Parameters
    -------------------
    h_alpha : array
        array of integers denoting hook-lengths of the box α in the Young diagram of λ
        If it is empty , then λ is considered as (n,n) .

    """
    if(len(h_alpha) == 0):
        return catalan(n)
    else:
        h_alpha_product = 1
        for i in h_alpha:
            h_alpha_product *= i
        if(factorial(n) % h_alpha_product != 0):
            raise ValueError(
                "Incorrect values of hook-lengths"
            )
        return int(factorial(n) / h_alpha_product)

def macmahon(a , b , c):
    """
    Returns MacMohan formula for the number M(a,b,c).
    It is equal to the number of plane partitions that fit in an (a×b×c) box.

    Parameters
    ----------
    a : int
        denotes length of box
    b : int
        denotes breadth of box
    c : int
        denotes height of box
    return  : int
        returns value of MacMohan formula

    """
    if(a!=int(a) or b!=int(b) or c!=int(c)):
        raise ValueError(
            "dimnsions must be positive integer"
        )
    ans = 1
    for i in range(1,a+1):
        for j in range(1,b+1):
            for k in range(1,c+1):
                ans *= (i+j+k-1)/(i+j+k-2)
    return ans

def dehn_sommerville(k , d):
    """
    Return coefficients of Dehn-Sommerville equations.
    Dehn-Sommerville equation is represented as : f(k−1) = ∑(i=k to i=d) C(i) * f(i−1), where C(i) represent coefficients.

    Parameters
    ----------
    k : int
        represent k in Dehn-Sommerville equation
    d : int
        denotes number of dimensions
    return  : dictionary
        key represent f(i-1)
        value denotes its coefficient

    """
    if(d < k):
        raise ValueError(
            "d cannot be smaller than k"
        )
    coeff = {}
    for i in range(k,d+1):
        coeff[i-1] = int((math.pow(-1 , d-i)) * binomialCoef(i , k))
    return coeff

def vershik_kerov_logan_shepp(n):
    """
    Returns asymptotic value of ℓn for large n.
    For a permutation σ∈Sn, let ℓ(σ) denote the maximal length of an increasing subsequence in σ. 
    Define ℓn = (1/n!) * ∑(σ∈Sn) ℓ(σ),
    the average value of ℓ(σ) for a σ chosen uniformly at random from Sn.

    Parameters
    ----------
    n : int
        denotes n in vershik equation as stated above
    return : float
        returns float number denoting asymptotic value of ℓn.

    """
    if(n != int(n)):
        raise ValueError(
            "n must be integer"
        )
    
    return 2 * math.sqrt(n)

def matrix_tree(n , eigenvalue_array):
    """
    Returns number of spanning trees of graph G.
    G is a graph of size n, let λ1≥…≥λn-1 be the eigenvalues of its Laplacian matrix.

    Parameters
    ----------
    n : int
        size of graph G
    eigenvalue_array : array
        array of integers having (n-1) eigenvalues of laplacian matrix of graph G.

    """
    if(len(eigenvalue_array) != n-1):
        raise ValueError(
            "number of eienvalues must be n-1"
        )
    
    if(n != int(n)):
        raise ValueError(
            "n must be positive intger"
        )
    
    ans = 1
    for i in range(len(eigenvalue_array)):
        ans *= eigenvalue_array[i]
    
    if(ans%n != 0):
        raise ValueError(
            "Wrong eigenvalues"
        )

    return int(ans/n)

def ramanujan_hardy_asymptotic(n):
    """
    Returns the value of Ramanujan-Hardy asymptotic formula for the number of partitions p(n) of n (for large n).

    Parameters
    ----------
    n : int 
        denotes positive integer
    return : int
        returns an integer denoting asymptotic value of p(n)

    """
    if(n != int(n)):
        raise ValueError(
            "n must be integer"
        )
    
    return int((1/(4*n*math.sqrt(3)))*math.exp(math.sqrt(2*n/3)))

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

def waerden_permanent_bound(n):
    """
    Returns lower bound for a doubly stochastic matrix A of size n×n.
    A square matrix with non-negative entries is said to be doubly stochastic if every row and every column sums up to 1.

    Parameters
    ----------
    n : int
        denotes nxn doubly stochastic matrix
    return : float
        returns lower bound for the permanent of the matrix

    """
    if(n!=int(n) or n<1):
        raise ValueError(
            "n must be positive integer"
        )
    return factorial(n)/math.pow(n,n)

def tutte(n):
    """
    Returns the number of rooted planar maps with n edges.

    Parameters:
    n : int
        denotes number of edges
    return : int
        returns an integer denoting number of rooted planar maps

    """
    if(n!=int(n) or n<1):
        raise ValueError(
            "n must be positive integer"
        )
    catalan_val = catalan(n)
    return int((2*(math.pow(3,n))*catalan_val)/(n+3))

