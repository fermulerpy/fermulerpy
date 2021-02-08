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

