"""
https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/
Hints: https://www.lucainvernizzi.net/blog/2014/11/21/codility-beta-challenge-number-of-disc-intersections/

[(-4, 1), (-1, 1), (0, 1), (0, 1), (1, -1), (2, 1), (4, -1), (4, -1), (5, 1), (5, -1), (6, -1), (8, -1)]

sol:    1        2        3      4       (3)       4       (3)      (2)      3       (2)      (1)      (0)
    
1 + 2 + 3 + 4 + 4 + 3 - (len(sol-with-no-brackets)) = 17 - 6 = 11
"""


def solution(A):
    events = []
    for center, radius in enumerate(A):
        events += [(center-radius, +1), (center+radius, -1)]
    events.sort(key=lambda x: x[0])

    # accumulate 1's
    number_of_disc_starts = 0
    number_of_intersections = 0
    number_of_terms_added = 0
    for _, begin_or_end in events:
        if begin_or_end == 1:
            number_of_disc_starts += 1
            number_of_intersections += number_of_disc_starts
            number_of_terms_added += 1
        else:
            number_of_disc_starts = number_of_disc_starts - 1

    total_intersections = number_of_intersections - number_of_terms_added
    if total_intersections > 10E6:
        total_intersections = -1

    return total_intersections


assert solution([1, 5, 2, 1, 4, 0]) == 11, f"First Failed"
assert solution([1, 0, 0, 3]) == 4, f"Second Failed"
assert solution([1, 1, 1]) == 3, f"Third Failed"
