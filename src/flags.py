def _find_all_peaks(A):
    all_peak_idx = list()
    for idx in range(len(A)):
        if idx == 0:
            if A[idx + 1] < A[idx]:
                all_peak_idx.append(idx)
        elif idx == len(A) - 1:
            if A[idx - 1] < A[idx]:
                all_peak_idx.append(idx)
        else:
            if (A[idx] > A[idx - 1]) and (A[idx] > A[idx + 1]):
                all_peak_idx.append(idx)
    print(f"All Peaks: {all_peak_idx}")
    return all_peak_idx


def solution(A):
    # O(N)
    all_peak_idx = _find_all_peaks(A)

    number_of_flags = len(all_peak_idx)

    for number_of_flags_ in range(number_of_flags, 0):
        if number_of_flags_ <

    # Can always put 1 flag if there exists a peak


assert 3 == solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2])
