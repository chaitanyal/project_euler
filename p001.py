#!/usr/local/bin/python3
"""Calculate sum of all multiples of 3 and 5 below 1000"""

def sum_divisible_by(divisor, num):
    """sum up numbers divisble by n from 1 to r"""
    return divisor * num * (num + 1)/2

def elegant_compute(num):
    """Constant time computation of sum of all multiples of 3 and 5 below max number"""
    k = num - 1
    sum_3 = sum_divisible_by(3, int(k/3))
    sum_5 = sum_divisible_by(5, int(k/5))
    sum_15 = sum_divisible_by(15, int(k/15))

    return sum_3 + sum_5 - sum_15


def brute_force_compute(num):
    """Brute force computation of sum of all multiples of 3 and 5 below max number"""
    all_multiples_3_5 = [i for i in range(1, num) if i % 3 == 0 or i % 5 == 0]
    return sum(all_multiples_3_5)

if __name__ == "__main__":
    NUM = 1000
    print("Brute force solution {0}".format(brute_force_compute(NUM)))
    print("Elegant solution {0}".format(elegant_compute(NUM)))
