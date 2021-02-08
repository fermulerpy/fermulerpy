import math

import random

import warnings

from fermulerpy.elementary import gcd, isDivisible

def rational_sol(*args):
    """
    Returns rational solutions for linear diophantine equation ax + by = c

    Parameters
    ----------
    *args : tuple
        Expects three arguments and optionally fourth argument.
        First three arguments denotes a, b and c respectively in ax + by = c

    Optional Parameters
    -------------------
    fourth argument in *args : int
        denotes number of solutions user wants

    Return
    ------
    if fourth argument not given : 1-d array
        returns one solution in the form of 1-d array [x,y]
    fourth argument given : 2-d array
        returns 2-d array of solutions

    """
    if(len(args)==3):
        a = args[0]
        b = args[1]
        c = args[2]
        x = random.randint(1,7) + math.pow(0.2,random.randint(2,4))

        if(a == 0 and b == 0):
            return []
        elif(a == 0 and b != 0):
            return [round(random.randint(1,7) + math.pow(0.2,random.randint(2,4)),2),c/b]
        elif(a != 0 and b == 0):
            return [c/a,round(random.randint(1,7) + math.pow(0.2,random.randint(2,4)),2)]

        y = (c - a*x)/b
        return [x,y]


    elif(len(args)==4):
        a = args[0]
        b = args[1]
        c = args[2]
        n = args[3]
        sol_arr = []

        if(a == 0 and b == 0):
            return []
        elif(a == 0 and b != 0):
            for i in range(n):
                sol_arr.append([round(random.randint(1,1000) + math.pow(0.2,random.randint(2,4)),2),c/b])
            return sol_arr
        elif(a != 0 and b == 0):
            for i in range(n):
                sol_arr.append([c/a,round(random.randint(1,7) + math.pow(0.2,random.randint(2,4)),2)])
            return sol_arr

        x = round(random.randint(1,7) + math.pow(0.2,random.randint(2,4)),2)

        for i in range(n):
            y = (c - a*x)/b
            sol_arr.append([x,y])
            x += 0.1
            x = round(x,2)
        return(sol_arr)


    elif(len(args)>4 or len(args)<3):
        raise NotImplementedError(
            "Invalid Number Of Arguments"
        )

def isInteger_sol(a , b ,c):
    """
    Checks if integer solution exist for ax + by = c

    Parameters
    ----------
    a : int
        denotes a in ax + by = c
    b : int
        denotes b in ax + by = c
    c : int
        denotes c in ax + by = c
    return : bool
        return true if integer solution exist otherwise false

    """
    return isDivisible(gcd(a,b),c)

# def integer_sol(a,b,c)