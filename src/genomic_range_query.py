def _parse_positions(S, M):
    """
    returns the index in S of the marker M
    """
    all_locations = set()
    for index in range(0, len(S)):
        if S[index] is M:
            all_locations.add(index)

    return all_locations


def _marker_exists_in_range(P, Q, AllPositions):
    query_set = set([x for x in range(P, Q + 1)])
    return query_set.intersection(AllPositions)


def solution(S, P, Q):
    all_A_Positions = _parse_positions(S, 'A')
    all_C_Positions = _parse_positions(S, 'C')
    all_G_Positions = _parse_positions(S, 'G')
    all_T_Positions = _parse_positions(S, 'T')

    assert len(P) == len(Q)
    result = list()
    for index_of_query in range(0, len(P)):
        if _marker_exists_in_range(P[index_of_query], Q[index_of_query], all_A_Positions):
            result.append(1)
        elif _marker_exists_in_range(P[index_of_query], Q[index_of_query], all_C_Positions):
            result.append(2)
        elif _marker_exists_in_range(P[index_of_query], Q[index_of_query], all_G_Positions):
            result.append(3)
        elif _marker_exists_in_range(P[index_of_query], Q[index_of_query], all_T_Positions):
            result.append(4)

    return result


assert [2, 4, 1] == solution('CAGCCTA', [2, 5, 0], [4, 5, 6])
assert [] == solution('', [2, 5, 0], [4, 5, 6])
assert [] == solution('C', [2, 5, 0], [4, 5, 6])
