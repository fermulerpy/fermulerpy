import math
import warnings

def quad_congruence_solve(a,p):
    """
    Return solutions of the quadratic congruences of the form x^2 ≡ a(mod p)

    Parameters
    ----------
    a : int
        denotes positive integer n in x^2 ≡ a(mod p)
    p : int
        denotes positive integer p in x^2 ≡ a(mod p)
    return : array
        returns an array of solutions of x^2 ≡ a(mod p)
        returns -1 if solutions does not exist

    """
    if(a!=int(a) or a<1 or p!=int(p) or p<1):
        raise ValueError(
            "n and p must be positive integer"
        )
    t = int((p-1)/2)
    if(pow(a,t,p) != 1):
        return -1
    
    while(True):
        t = int(math.sqrt(a))
        if(t*t == a):
            break
        a = a + p
    sol = []
    s1 = int(math.sqrt(a))
    sol.append(s1)
    sol.append(p-s1)
    sol = sorted(sol)
    return sol

