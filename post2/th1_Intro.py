import sys
from typing import Tuple, no_type_check


def dynamically_typed(li):
    sum_list = sum(li)
    return "Dynamically typed method", sum_list


def type_checked(li: list[int]) -> Tuple[str, int]:
    sum_list = sum(li)
    return "Type checked method", sum_list


@no_type_check
def type_check_ignored(li: list[int]) -> Tuple[int, int]:
    sum_list = sum(li)
    return "Type check ignored method", sum_list


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing list argument of the type 10,20,40.")
    else:
        li_str = sys.argv[1]
        li_list = [int(i) for i in li_str.split(',')]
        methods = [dynamically_typed, type_checked, type_check_ignored]
        for method in methods:
            how, result = method(li_list)
            print(f"{how} Sum = {result}")
