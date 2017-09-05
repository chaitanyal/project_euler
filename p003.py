#!/usr/local/bin/python3
"""Find the largest prime factor of the number 600851475143 ?"""

import math

def is_prime(num):
    """Determines if num is prime number or not"""

    # 0 and 1 are not prime numbers
    if num < 2:
        return False

    # 2 is the only even prime number
    if num == 2:
        return True

    # all other even numbers are not prime
    if not num & 1:
        return False

    for i in range(3, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def elegant_compute(num):
    """elegant solution to compute max prime factor using fundamental theorem of arithmetic"""
    # https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
    return num


def brute_force_compute(num):
    """brute force solution to compute max prime factor"""
    factors = [i for i in range(1, int(num / 2)) if num % i == 0]
    factors.append(num)
    prime_factors = [i for i in factors if is_prime(i)]
    print(factors)
    print(prime_factors)
    return max(prime_factors)


if __name__ == "__main__":
    NUM = 72
    print(brute_force_compute(NUM))
