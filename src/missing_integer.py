"""
Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
"""
import sys


def solution(A):
    smallest_integer: int = sys.maxsize

    # discard all the negative numbers
    A.sort()
    #A_ = [x for x in A if x > 0]

    # A.sort()
    if A[len(A) - 1] <= 0 or A[0] > 1:
        return 1

    else:
        # now loop: Loop through N elements is divided into two parts
        #
        # Find the index from where positive numbers start to appear
        for i in range(0, len(A)):
            if A[i] <= 0:
                continue
            else:
                break

        expectedInteger = A[i]
        if expectedInteger > 1:
            return 1

        for j in range(i, len(A)):
            if not (A[j] == expectedInteger or A[j] == expectedInteger + 1):
                return expectedInteger + 1
            else:
                expectedInteger = A[j]

        if j == len(A) - 1:
            # ran out of loop
            return expectedInteger + 1


assert 1 == solution([-1, -2, -4]), f"First Assert Failed"
assert 3 == solution([1, 2, 4]), f"Second Assert Failed"
assert 1 == solution([0, 0, 0]), f"Third Assert Failed"
assert 5 == solution([1, 3, 6, 4, 1, 2]), f"Fourth Assert Failed"
assert 5 == solution([-1, 3, -6, 4, 1, 2]), f"Fifth Assert Failed"
assert 1 == solution([99, 199, 2000]), f"Sixth Assert Failed"
assert 1 == solution([-1000, 1000]), f"Seventh Assert Failed"
