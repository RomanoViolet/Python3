import sys


def solution(A):
    A.sort()
    unique_values = 0
    previous_value = sys.maxsize
    for i in A:
        if i != previous_value:
            unique_values += 1
            previous_value = i
    return unique_values


assert 3 == solution([1, 2, 3, 3, 3, 1, 2])
assert 3 == solution([2, 1, 1, 2, 3, 1])
assert 2 == solution([1, 1, 1, 1, 1, 3])
assert 1 == solution([1, 1, 1, 1, 1, 1])
