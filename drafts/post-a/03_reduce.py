
import time
import functools
import math 
import rich
from rich.console import Console
from rich.text import Text

console = Console()
error_console = Console(stderr=True, style="bold red")

@functools.lru_cache
def factorial_cache(n):
    if n <= 0:
        return 1
    return n*factorial_cache(n-1)

def factorial_sum_cache(_sum, n):
    return _sum + factorial_cache(n)

def format_factorial(f):
    f = str(f)
    return f[0:4]+f"...{len(f)-8} digits..."+f[-4:]


def time_factorial_sum_cache(n):
    try:
        start = time.time()
        Factorial = functools.reduce(factorial_sum_cache, list(range(1,n+1)))
        if len(str(Factorial))<12:
            Factorial_Sum = Factorial
        else:
            Factorial_Sum = format_factorial(Factorial)
        console.log(f"Time taken for factorial_sum_cache for {n=} -> {time.time()-start:0.20f} s. {Factorial_Sum=}".format())
    except Exception as e:
        console.log(f"Error in factorial_sum_no_cache = {e}")
