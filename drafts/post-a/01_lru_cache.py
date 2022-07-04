import time
import functools
import math 
import sys
import rich
from rich.console import Console
from rich.text import Text

console = Console()
error_console = Console(stderr=True, style="bold red")

timers = {}
def timer(func):
    def inner_dec(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        console.log(f"Time taken for {func.__name__} for {n=} -> {time.time()-start:0.20f} s".format())
        return f
    return inner_dec


# max_size = 3 etc can be set as params for lru_cache


@functools.lru_cache
def factorial_cache(n):
    if n == 0:
        return 1
    return n*factorial_cache(n-1)

def factorial_no_cache(n):
    if n == 0:
        return 1
    return n*factorial_no_cache(n-1)

def factorial_math(n):
    return math.factorial(n)

def factorial_sum_math(n):
    _sum = 0
    for i in range(1,n):
        _sum = _sum + factorial_math(i)
    return _sum

def factorial_sum_cache(n):
    _sum = 0
    for i in range(1,n):
        _sum = _sum + factorial_cache(i-1)*i
    return _sum

def factorial_sum_no_cache(n):
    _sum = 0
    for i in range(1,n):
        _sum = _sum + factorial_no_cache(i-1)*i
    return _sum

@timer
def time_factorial_sum_math(n):
    try:
        factorial_sum_math(n)
    except Exception as e:
        console.log(f"Error in factorial_sum_no_cache = {e}")


def time_factorial_sum_no_cache(n):
    try:
        start = time.time()
        factorial_sum_no_cache(n)
        console.log(f"Time taken for factorial_sum_no_cache for {n=} -> {time.time()-start:0.20f} s".format())
    except Exception as e:
        console.log(f"Error in factorial_sum_no_cache for {n} = {e}")

def time_factorial_sum_cache(n):
    try:
        start = time.time()
        factorial_sum_cache(n)
        console.log(f"Time taken for factorial_sum_cache for {n=} -> {time.time()-start:0.20f} s".format())
    except Exception as e:
        console.log(f"Error in factorial_sum_no_cache = {e}")



if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Runtime argument missing - Usage : python lru_cache.py <int>")
    n = int(sys.argv[1])
    time_factorial_sum_math(n)
    time_factorial_sum_no_cache(n)
    time_factorial_sum_cache(n)










