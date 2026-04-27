def isprime(n):
    """
    Determine whether a number is prime.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isperfect(n):
    """
    Determine whether a number is a perfect number.

    A perfect number is a positive integer that is equal to the sum of its proper divisors (divisors excluding the number itself).
    For example, 6 is perfect because 1 + 2 + 3 = 6.

    Args:
        n (int): The number to check for perfection.

    Returns:
        bool: True if n is a perfect number, False otherwise.
    """
    if n < 2:
        return False
    sum_of_divisors = 1
    for i in range(2, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n


def print_all_factors(n):
    """
    Print all factors of a given positive integer.

    Factors are all positive integers that divide the given number evenly (with no remainder).

    Args:
        n (int): The number for which to find and print all factors.

    Returns:
        None: This function prints to stdout but does not return a value.
    """
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    print(f"Factors of {n}: {factors}")