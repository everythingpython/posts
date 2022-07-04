from functools import singledispatch

@singledispatch
def add(arg):
    raise NotImplementedError("Unsupported type")

@add.register(int)
def _(a, b):
    return f"Sum = {a+b}"

@add.register(str)
def _(a, b):
    return f"Resultant sentence = {a+' '+b}"

print(add(1,2))
print(add("Hello", "Goodbye"))