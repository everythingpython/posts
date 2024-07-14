import sys


def add(a, b):
    dict_ = {"num1": a, "num2": b}
    ret_val = dict_["num1"] + dict_["num2"]
    return ret_val


a, b = int(sys.argv[1]), int(sys.argv[2])
print(add(a, b))
