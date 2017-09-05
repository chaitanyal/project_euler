#!/usr/local/bin/python3
"""Find sum of even valued terms in Fibonacci sequence whose values do not exceed 4 million"""
import functools

@functools.lru_cache(maxsize=None)
def fibonacci(num):
    """Fibonacci number. Uses memoization to run faster."""
    if num < 2:
        return 1

    return fibonacci(num - 1) + fibonacci(num - 2)

def non_recursive_fibonacci(num):
    """Non recursive implementation of Fibonacci number."""

    if num < 2:
        return 1

    result = 0
    fib1 = 1
    fib2 = 1

    while num >= 2:
        num = num - 1
        result = fib1 + fib2
        fib1, fib2 = fib2, result

    return result

def compute(num):
    """sum of the even-valued fibonacci terms not exceeding max_num"""
    i = 2
    ans = 0

    while ans <= num:
        n = fibonacci(i)
        #n = non_recursive_fibonacci(i)
        ans += n
        #every 3rd fibonacci term is even - 1 1 2 3 5 8 13 21 34
        i = i + 3

    return ans

if __name__ == "__main__":
    NUM = 4 * 10**6 #4 million = 4 * 10^6
    print(compute(NUM))
    print(fibonacci.cache_info()) #see number of cache hits/misses due to memoization
