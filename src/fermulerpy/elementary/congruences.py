import math

def isCongruent(a , b , m):
    """
    Checks if a is congruent to b modulo m i.e., a ≡ b (mod m)

    Parameters
    ----------
    a : int
        denotes a in equation a ≡ b (mod m)
    b : int
        denotes b in eqaution a ≡ b (mod m)
    m : int
        denotes m in equation a ≡ b (mod m)
    return : bool
        return true if a is congruent to b modulo m otherwise false

    """
    return (a%m) == (b%m)

def least_residue(a , m):
    """
    Returns least residue of a (mod m)

    Parameters
    ----------
    a : int
        denotes a in a (mod m)
    m : int
        denotes m in a (mod m)
    return : int
        returns integer least residue

    """
    return a%m

def congruence_props():
    """
    Prints basic properties of congruencies

    Parameters
    ----------
    It takes no input arguments
    return : Null
        It just prints out properties of congruences

    """
    print("Five general properties of congruence : ")
    print("a ≡ a (mod m)")
    print("If a ≡ b (mod m), then b ≡ a (mod m)")
    print("If a ≡ b (mod m) and b ≡ c (mod m), then a ≡ c (mod m)")
    print("If a ≡ b (mod m) and c ≡ d (mod m), then a + c ≡ b + d (mod m)")
    print("If a ≡ b (mod m) and c ≡ d (mod m), then ac ≡ bd (mod m)")

