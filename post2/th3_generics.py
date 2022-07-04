"""
About type vars
"""
import sys
from typing import TypeVar, Any


class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b


T = TypeVar("T")
T2 = TypeVar("T2", Rectangle, Any)
T3 = TypeVar("T3", str, float)


def area(r: T) -> T:
    return r.length * r.breadth


def area2(r: T2) -> T2:
    return r.length * r.breadth


def area3(r: Any) -> T3:
    return r.length * r.breadth


def area4(r: str) -> bool:
    return r.length * r.breadth


if len(sys.argv) < 2:
    raise ValueError("Not enough parameters")
l, b = [int(i) for i in sys.argv[1].split(",")]
r1 = Rectangle(l, b)
functions = [area, area2, area3]
for f in range(len(functions)):
    print(f"Area using func{f + 1} = {functions[f](r1)}")
print(f"Area using func4 = {area4(r1)}")