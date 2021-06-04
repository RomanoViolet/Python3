def solution(N, A):
    # N: Number of counters
    # A: Coded operations
    all_counters = [0] * N
    current_max = 0
    for this_operation in A:
        # given that 1 <= this_operation <= N
        if this_operation <= N:
            # increase an individual counter
            all_counters[this_operation - 1] += 1
            if all_counters[this_operation - 1] > current_max:
                current_max = all_counters[this_operation - 1]
        else:
            # set all counters to current max.
            all_counters = [current_max] * N

    return all_counters


assert [3, 2, 2, 4, 2] == solution(5, [3, 4, 4, 6, 1, 4, 4])
assert [6, 0, 0, 0, 0] == solution(5, [1, 1, 1, 1, 1, 1])
assert [4, 1, 0, 0, 0] == solution(5, [6, 1, 1, 2, 1, 1])
assert [1, 1, 1, 1, 1] == solution(5, [1, 2, 3, 4, 5, 6])
assert [0, 0, 0, 0, 0] == solution(5, [6])
assert [1, 0, 0, 0, 0] == solution(5, [1])
