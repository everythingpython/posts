"""
Instantiating Generic Classes and Type Erasure
"""
from typing import TypeVar, Generic, no_type_check

T = TypeVar('T')
subject_master = {1: "Algorithms",
                  2: "Graph Theory",
                  3: "Data Structures"}

subject_master_alt = {"a": "Algorithms",
                      "g": "Graph Theory",
                      "d": "Data Structures"}

faculty_master = {"Algorithms": "Prof.Flitwick",
                  "Graph Theory": "Dr.Binns",
                  "Data Structures": "Dr.McGonagall"}


class ComputerScience(Generic[T]):
    def __init__(self, subject_id: T) -> None:
        type_id = type(subject_id).__name__
        match type_id:
            case "int":
                self.subject_name = subject_master[subject_id]
            case "str":
                self.subject_name = subject_master_alt[subject_id]
        self.subject_id = subject_id

    def get_faculty(self):
        try:
            return faculty_master[self.subject_name]
        except KeyError:
            return None


# Types inferred for next 2 statements below

c1 = ComputerScience(2)
c2 = ComputerScience("a")

# Instantiating a concrete type

c3 = ComputerScience[int](3)
c4 = ComputerScience[str]("d")

cs_objects = [c1, c2, c3, c4]
for i in cs_objects:
    print(f"{i.subject_name} is being taught by {i.get_faculty()}")

