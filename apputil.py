import seaborn as sns
import pandas as pd


# update/add code below ...
print("apputil.py loaded")


# the following 2 lines are an optimization for the Fibonacci function
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    else: return fib(n-1) + fib(n-2)
print(fib(50))



def to_binary(n):
    # binary of n <= 1 is n
    if n <= 1: return n
    else: return (
        to_binary(n%2)  # returns the remainder of n divided by 2, e.g. 5%2 = 1, 4%2 = 0; 
                   #any modulus 2 is either 0 or 1, giving us the first (rightmost) binary digit
        + 10*to_binary(n//2) # integer division, e.g. 5//2 = 2; 
                        # for any other number, get the floor of n/2, and multiply the result by 10 to shift left in binary
    )

# testing 
print(to_binary(255))
