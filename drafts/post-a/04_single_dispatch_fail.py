from functools import singledispatch

@singledispatch
def join(arg):
    raise NotImplementedError("Unsupported type")

@join.register
def _(arg_list: list[int], delimiter):
    return delimiter.join([str(i) for i in arg_list])

@join.register
def _(arg_list : list[str], delimiter):
    return delimiter.join(arg_list)

print(join(["This","is","alright"]," "))
print(join([0,1,1,8],'-'))