impact = {
    'A': 1,
    'C': 2,
    'G': 3,
    'T': 4
}


def get_min(counts, p, q):
    for key in 'A', 'C', 'G', 'T':
        p_count = counts[key][p-1] if p > 0 else 0
        if (counts[key][q] - p_count > 0):
            return impact[key]


def solution(S, P, Q):
    N = len(S)
    counts = dict(
        A=[0] * N,
        C=[0] * N,
        G=[0] * N,
        T=[0] * N)
    for i in range(N):
        for key in counts:
            counts[key][i] = counts[key][i-1]
        counts[S[i]][i] += 1
    return [get_min(counts, p, q) for p, q in zip(P, Q)]


assert [2, 4, 1] == solution('CAGCCTA', [2, 5, 0], [4, 5, 6])
#assert [] == solution('', [2, 5, 0], [4, 5, 6])
