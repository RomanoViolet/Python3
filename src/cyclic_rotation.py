def solution(A, K):
    A_ = [0] * len(A)

    for i in range(0, len(A)):
        # index i goes to i+3 % len(A)
        A_[(i + K) % len(A)] = A[i]

    return A_


assert [9, 7, 6, 3, 8] == solution([3, 8, 9, 7, 6], 3)
assert [1, 2, 3, 4] == solution([1, 2, 3, 4], 4)
assert [0, 0, 0] == solution([0, 0, 0], 1)
