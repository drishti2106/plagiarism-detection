# testC_fact.py

"""
This module calculates factorial using iteration.
Author: Student X
"""

def factorial(n):  # n is non-negative integer
    result = 1    # initialize result
    for i in range(1, n + 1):  # loop from 1 to n
        result *= i           # multiply each step
    return result

if __name__ == "__main__":
    print(factorial(5))  # display
