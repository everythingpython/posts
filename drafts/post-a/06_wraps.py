import functools

# Wraps is a decorator that updates a wrapper function's attributes to make it look like the wrapped function.

def deco(func):
    @functools.wraps(func)
    def inner_dec(*args, **kwargs):
        print("Inside inner_dec")
        return func(*args, **kwargs)
    return inner_dec


@deco
def f(s :str):
    """Just printing Sparta"""
    print(f"This is {s}")

if __name__ == "main":
    f("Sparta")