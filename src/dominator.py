def solution(A):
    if not A:
        return -1

    A_ = A.copy()

    # lg(N)
    A_.sort()

    candidate = A_[int(len(A)/2)]

    # N
    count = 0
    for i_ in A_:
        if i_ == candidate:
            count += 1

    if count > len(A_)/2:
        leader = candidate
    else:
        leader = None

    # N
    if leader is not None:
        for i_ in range(len(A)):
            if A[i_] == leader:
                return i_
    else:
        return -1


assert 0 == solution([3, 4, 3, 2, 3, -1, 3, 3])
assert -1 == solution([1, 2, 3])
assert -1 == solution([])
assert 0 == solution([1])
assert 0 == solution([1, 1, 1, 1, 1])
