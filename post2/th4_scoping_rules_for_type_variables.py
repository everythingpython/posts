"""
Scoping Rules for Type Variables
"""
from typing import TypeVar, Generic, List, Union, Any

T = TypeVar('T', int, float, Any)
S = TypeVar('S', int, float)


def fun_1(x: T) -> None:
    """T can be anything"""
    print(f"Floating point value : {x}")


def fun_2(x: T) -> None:
    """T can be anything"""
    print(f"String value : {x}")


class GenericTest(Generic[T]):
    """Expecting to be sent floats for both functions
     because the class was specified to say that T was of type float"""

    def g_func1(self, x: T) -> None:
        print(f"Floating point value : {x}")

    def g_func2(self, x: T) -> None:
        print(f"String value from g_func2 : {x}")


def unbound_types(x: T) -> None:
    y1 = []  # type: List[T] # This is okay
    y2 = []  # type: List[S] # This is Not


def bound_type(x: Union[T, S]) -> None:
    z1 = []  # type: List[T] # This is okay
    z2 = []  # type: List[S] # This is Also okay


fun_1(1.0)  # Sending float
fun_2("String sent")  # Sending string

gt = GenericTest()  # type: GenericTest[float]
gt.g_func1(10.0)  # Sending float
gt.g_func2("Whoops")  # Sending string when float was expected. mypy should flag this.
gt.g_func2(15.0)  # Sending float as expected.
unbound_types(10)
bound_type(10)
