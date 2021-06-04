import sys


def golden_max_slice(A):
    max_slice = A[0]
    #trace = list()
    # trace.append(max_slice)
    value_of_max_slice = -sys.maxsize
    for idx in range(1, len(A)):
        # Choose whether to start a new slice here, or to combine with previous slices
        max_slice = max(max_slice + A[idx], A[idx])
        if max_slice > value_of_max_slice:
            value_of_max_slice = max_slice
        # trace.append(max_slice)
    return value_of_max_slice


assert 10 == golden_max_slice([5, -7, 3, 5, -2, 4, -1])
assert 6 == golden_max_slice([-2, 1, -3, 4, -1, 2, 1, -5, 4])
