import functools

# Decorators extend/alter a function and return it. 

def deco(func):
    def inner_dec(*args, **kwargs):
        print("Inside inner_dec")
        return func(*args, **kwargs)
    return inner_dec


@deco
def f(s :str):
    """Just printing Sparta"""
    print(f"This is {s}")

if __name__ == "__main__":
    f("Sparta")