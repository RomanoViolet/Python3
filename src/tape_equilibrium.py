import sys


def solution(A):
    sum_A: int = sum(A)
    left_sum: int = 0
    right_sum: int = sum_A
    gap: int = sys.maxsize
    for left_border_index in range(0, len(A)-1):
        left_border_number = A[left_border_index]
        left_sum += left_border_number
        right_sum = sum_A - left_sum
        curret_gap = right_sum - left_sum
        if abs(curret_gap) < gap:
            gap = abs(curret_gap)
    return gap


assert 1 == solution([3, 1, 2, 4, 3]), f"First case failed."
assert 0 == solution([0, 0]), f"Second case failed."
assert 1 == solution([3, 1, 1]), f"Third case failed."
assert 1 == solution([1, 1, 1]), f"Fourth case failed."
assert 2000 == solution([-1000, 1000]), f"Fourth case failed."
