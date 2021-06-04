import sys


def golden_max_slice(A):
    max_slice = A[0]
    value_of_max_slice = -sys.maxsize
    start_idx = 0
    end_idx = 0
    for idx in range(1, len(A)):
        # Choose whether to start a new slice here, or to combine with previous slices
        if max_slice+A[idx] > A[idx]:
            # keep the previous start_idx
            #end_idx = idx
            pass
        else:
            start_idx = idx
            end_idx = idx
        max_slice = max(max_slice + A[idx], A[idx])
        if max_slice > value_of_max_slice:
            value_of_max_slice = max_slice
            end_idx = idx
        # trace.append(max_slice)
    return [start_idx, end_idx, value_of_max_slice]


def solution(A):
    # find the maximum slice
    [start, end, value] = golden_max_slice(A)

    # Split the array from 0:start-1, and end+1: len(A)
    start_left = -1
    if start > 1:
        [start_left, end_left, value_left] = golden_max_slice(A[0:start-1])
    start_right = -1
    if end < len(A) - 1:
        [start_right, end_right, value_right] = golden_max_slice(
            A[end+1, len(A)])

    left_combo = None
    if start_left != -1:
        left_combo = value + value_left

    right_combo = None
    if start_right != -1:
        right_combo = value + value_right

    if left_combo is None and right_combo is not None:
        return right_combo
    if right_combo is None and left_combo is not None:
        return left_combo
    else:
        return value


assert 17 == solution([3, 2, 6, -1, 4, 5, -1, 2])
