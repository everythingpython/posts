import functools

# Only need to implement ONE of __lt__(), __le__(), __gt__(), or __ge__() AND __eq__()

@functools.total_ordering
class A:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value < other.value
    def __eq__(self, other):
        return self.value == other.value

print(A(1) < A(2))
print(A(2) > A(1))
print(A(1) <= A(2))
print(A(2) >= A(1))
print(A(2) <= A(2))
print(A(2) >= A(2))
print(A(1) > A(2)) 