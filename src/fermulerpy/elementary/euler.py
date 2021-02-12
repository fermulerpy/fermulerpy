from fermulerpy.elementary import prime_divisors

def euler_function(n):
    """
    Returns value of euler function for n i.e., φ(n)

    Parameters
    ----------
    n : int
        denotes positive integer greater than 2
    return : int
        returns the value of φ(n)

    """
    prime_divisors_arr = prime_divisors(n)

    num = 1
    for i in prime_divisors_arr:
        num *= (i - 1)
    
    den = 1
    for i in prime_divisors_arr:
        den *= i
    
    return int((num * n)/den)

