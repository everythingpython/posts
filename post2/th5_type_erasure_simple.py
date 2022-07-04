"""
Instantiating Generic Classes and Type Erasure
"""
from typing import TypeVar, Generic, no_type_check

T = TypeVar('T')


class ComputerScience(Generic[T]):
    def __init__(self, subject_id: T) -> None:
        self.subject_id = subject_id


# Types inferred for next 2 statements below

c1 = ComputerScience(2)
c2 = ComputerScience("a")

# Instantiating a concrete type

c3 = ComputerScience[int](3)
c4 = ComputerScience[str]("d")

# Mismatched types and corresponding data. mypy isn't happy

c5 = ComputerScience[str](3)
c6 = ComputerScience[int]("d")

cs_objects = [c1, c2, c3, c4, c5, c6]

for i in cs_objects:
    print(f"{i.subject_id=}.")

