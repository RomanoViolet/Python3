def solution(A):
    A.sort()
    for i in range(0, len(A), 2):
        if i < len(A)-2:
            if A[i] != A[i+1]:
                return A[i]
        else:
            return A[i]


assert 3 == solution([1, 2, 3, 4, 5, 4, 2, 1, 5]), f" first assert failed"
assert 7 == solution([9, 3, 9, 3, 9, 7, 9]), f" second assert failed"
assert 1 == solution([0, 0, 0, 0, 0, 0, 1]), f" third assert failed"
assert 1 == solution([1, 0, 0, 0, 0, 0, 0]), f" fourth assert failed"
