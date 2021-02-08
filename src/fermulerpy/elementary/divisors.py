import math
import warnings
n=int(input("ENTER A NUMBER: "))

"""
    Finding all the divisors of a number
    function argument: input number n (natural number) 
    return : list(list of divisors of user given number)
"""
def get_divisors(n):
    if(n<=0):
        raise ValueError(
            "n must be a positive number"
        )
    list1=[]
    for i in range(1,n+1):
        if(n%i==0):
            list1.append(i)
    return list1
    
    
"""
    Finding total number of divisors of user given number
    function argument: input number n (natural number) 
    return : int (number of divisors)
"""
def divisor_count(n):
    if(n<=0):
        raise ValueError(
            "n must be a positive number"
        )
    
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    return count


"""
    Finding sum of all divisors of user given number
    function argument: input number n (natural number) 
    return : int (sum of all divisors)
"""
def divisor_sum(n):
    if(n<=0):
        raise ValueError(
            "n must be a positive number"
        )
    
    sum1=0
    for i in range(1,n+1):
        if(n%i==0):
            sum1+=i
    return sum1
    
