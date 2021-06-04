def solution(A):
    """
    Need to check only size-2 and size-3 slices as any larger slice can be combined by combining
    size-2 and size-3 slices. 
    Also, since the mean of two numbers (or, two non-overlapping slices) must lie between the mean of individual slices,
    therefore, finding min of size-2 and size-3 slices is sufficient.
    """
    import sys
    min_idx = -1
    global_min = sys.maxsize

    for i in range(len(A)-1):
        size_2_min = (A[i] + A[i+1])/2.0
        if global_min > size_2_min:
            global_min = size_2_min
            min_idx = i
        if i >= len(A) - 2:
            continue
        size_3_min = (A[i] + A[i+1] + A[i+2])/3.0
        if global_min > size_3_min:
            global_min = size_3_min
            min_idx = i

    return min_idx


assert 1 == solution([4, 2, 2, 5, 1, 5, 8])
assert 0 == solution([0, 0])
assert 0 == solution([0, 0, 1, 2])
