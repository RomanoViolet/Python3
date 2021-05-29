"""
Write a function:

    def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A ≤ B.

"""
import math


def solution(A: int, B: int, K: int):

    # smallest non zero dividend is the list
    smallest_ = math.ceil(A / K)

    # Largest non-zero dividend in the list
    largest_ = math.floor(B / K)

    # special cases
    if A == 0 and B == 0:
        return 1

    if smallest_ == 0 and largest_ == 0 and A <= 0:
        # range is too small but contains a zero
        total = 1
    elif smallest_ == 0 and largest_ == 0 and (B - A + 1) < K:
        # range too small, and no divisible number inside
        return 0
    else:
        total = largest_ - smallest_ + 1

    return total


assert 3 == solution(6, 11, 2), f"First assert failed."
assert 9 == solution(-6, 11, 2), f"Second assert failed."
assert 1 == solution(0, 0, 2), f"Third assert failed."
assert 3 == solution(-2, 2, 2), f"Fourth assert failed."
assert 1 == solution(-2, 2, 4), f"Fifth assert failed."
assert 0 == solution(1, 5, 7), f"Sixth assert failed."
assert 20 == solution(11, 345, 17), f"Seventh assert failed."
