import math
import warnings

from fermulerpy.utils import APRtest

def isPrime(num):
    """
    Checks if the number is prime

    Parameters
    ----------
    num : int
        denotes a natural number 
    return : bool
        return true if the number is prime otherwise returns false

    """
    if(num < 0):
        raise ValueError(
            "num must be a natural natural"
        )

    if(num <= 1):
        return False
    if(num <= 3):
        return True
    if(num%2 == 0 or num%3==0):
        return False
    x = num + 1
    if(x and (not(x & (x - 1)))): #Lucas-Lehmer Test
        p = 0
        c = 0
        while(x>=1):
            x /= 2
            c = c + 1
        p = c-1
        checkNumber = x
        nextval = 4 % checkNumber
        for i in range(1, p - 1):
            nextval = (nextval * nextval - 2) % checkNumber
        if (nextval == 0): return True
        else: return False

    return APRtest(num)

def prime_series(count):
    """
    Returns an array of prime numbers

    Parameters
    ----------
    count : int
        denotes the count of prime numbers
    return : array
        return an array of length 'count'

    """
    if(count < 0 or int(count)!=count):
        raise ValueError(
            "Input must be a non-negative integer"
        )
    if(count <= 5):
        arr_prime = []
        i = 0
        j = 2
        while(i < count):
            if(isPrime(j)):
                arr_prime.append(j)
                i = i + 1
            j = j + 1
        return arr_prime
    n = count
    upper = n*(math.log(n*math.log(n)))
    upper = math.floor(upper)
    arr = SieveOfEratosthenes(upper)
    arr_prime = arr[0:count]
    return arr_prime

def prime(n):
    """
    Returns n'th prime number

    Parameters
    ----------
    n : int
        denotes the position of prime number
    return : int
        returns an integer
    """
    if(n < 0 or int(n)!=n):
        raise ValueError(
            "Input must be a non-negative integer"
        )
    arr1 = [2,3,5,7,11,13]
    count = n
    if(count <= 6):
        return arr1[count-1]
    upper = n*(math.log(n*math.log(n)))
    upper = math.floor(upper)
    arr = SieveOfEratosthenes(upper)
    return arr[count-1]

def prime_table(count):
    """
    Returns an array of numbers of prime-table

    Parameters
    ----------
    count : int
        denotes a non-negative integer
    return : array
        returns an array of length 'count'

    """
    if(count < 0 or int(count)!=count):
        raise ValueError(
            "count must be a non-negative integer"
        )

    prime_array = prime_series(count)

    for i in range(1,len(prime_array)):
        prime_array[i] = prime_array[i] * prime_array[i-1]

    prime_table_array = [i+1 for i in prime_array]

    return prime_table_array

def SieveOfEratosthenes(*args):
    """
    Returns prime numbers within a range (including lower and upper bounds) or prime numbers less than or equal to given input

    Parameters
    ----------
    *args : tuple
        Expects one or two arguments as described below

    Other Parameters
    ----------------
    1 argument : int
        denotes upper bound for prime numbers
    2 arguments : (int,int)
        denotes lower and upper bounds for range of prime numbers
    
    Returns
    -------
    array
        returns an array of prime numbers

    """
    if(len(args)==1):
        n = args[0]
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        prime_arr = []    
        for p in range(2, n+1):
            if prime[p]:
                prime_arr.append(p)
        return prime_arr
    elif(len(args)==2):
        low = args[0]
        high = args[1]
        n = args[1]
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        prime_arr = []    
        for p in range(2, n+1):
            if (prime[p] and p>=low):
                prime_arr.append(p)
        return prime_arr
    elif(len(args)>2):
        raise NotImplementedError(
            "Invalid Number Of Arguments"
        )

def prime_divisors(n): 
    """
    Returns all prime divisors of a number

    Parameters
    ----------
    n : int
        denotes the positive integer of which prime divisors needs to be find out
    return : array
        returns an array of integers denoting prime divisors of n

    """
    arr = []  
    if(n<2):
        return arr

    while n % 2 == 0: 
        arr.append(2) 
        n = n // 2

    for i in range(3,int(math.sqrt(n))+1,2):  
        while n % i== 0: 
            arr.append(i)
            n = n // i

    if n > 2: 
        arr.append(n)

    if(len(arr) == 1):
        return arr
    else:
        temp_arr = []
        temp_arr.append(arr[0])
        for i in range(1,len(arr)):
            if(arr[i] != arr[i-1]):
                temp_arr.append(arr[i])
        return temp_arr

def findFrequency(A, freq):
    """
    It is a helper function
    """
    (left, right) = (0, len(A) - 1)
    while left <= right:
        if A[left] == A[right]:
            freq[A[left]] = freq.get(A[left], 0) + (right - left + 1)
            left = right + 1
            right = len(A) - 1
        else:
            right = (left + right) // 2

def prime_factorization(n):
    """
    Calculates unique prime factorization of given positive integer

    Parameters
    ----------
    n : int
        denotes the positive integer of which prime factorization needs to be calculated
    return : dictionary
        returns a dictionary in which key represent prime divisor and value represent its power

    """
    if(n<1):
        raise ValueError(
            "n must be a positive integer"
        )
    arr = []  
    if(n<2):
        return arr

    if(isPrime(n)):
        return {n:1}

    while n % 2 == 0: 
        arr.append(2) 
        n = n // 2

    for i in range(3,int(math.sqrt(n))+1,2):  
        while n % i== 0: 
            arr.append(i)
            n = n // i

    if n > 2: 
        arr.append(n)
    count = {}
    findFrequency(arr, count)
    return count

