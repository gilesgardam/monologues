import doctest
from math import factorial


def is_prime(n):
    """ Naive O(sqrt(n)) primality test.

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(6)
    False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    q = 3
    while q*q <= n:
        if n % q == 0:
            return False
        q += 2
    return True


def primes(n):
    """ Returns a list of the primes in range(n).

    >>> primes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> len(primes(100))
    25
    """
    if n < 2:
        return []
    primes = [2]
    p = 3
    while p < n:
        prime = True
        for q in primes:
            if q * q > p:
                break
            if p % q == 0:
                prime = False
                break
        if prime:
            primes.append(p)
        p += 2
    return primes


def choose(n, k):
    """ Computes the binomial coefficient n choose k.

    >>> choose(5, -1)
    0
    >>> choose(5, 0)
    1
    >>> choose(5, 1)
    5
    >>> choose(5, 2)
    10
    """
    if k < 0 or k > n:
        return 0
    return factorial(n) / factorial(k) / factorial(n-k)


if __name__ == '__main__':
    doctest.testmod()
