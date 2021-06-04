def _generate_sufficient_fibonacci_numbers(maxFib: int):
    """
    Since it is given that N <= 100,000, generate the first 23 fibonacci numbers and store those for reference
    Omit the repeating 1 at the beginning for brevity
    """
    fib = list()
    fib.append(1)
    fib.append(2)
    i = 2
    while True:
        fib.append(fib[i-1] + fib[i-2])
        if fib[i] > 100000:
            break
        else:
            i += 1

    return set(fib)


def _accumulate_jump_distances(A):
    """
    accumulates distances to jump, i.e., converts them to milestone distances.
    If A: * 0 0 0 1  1 0 1 0 0 0 0 * / *: start and end positions.
       D: |---4---|1 |-2-|----5----|
  """
    previous_bit = 0
    d = 0
    accumulated_positions = list()
    for pos in A:
        if pos == 0:
            previous_bit = pos
            d += 1
        if pos == 1:
            if pos == 1 and previous_bit == 0:
                if len(accumulated_positions) == 0:
                    accumulated_positions.append(d+1)
                else:
                    accumulated_positions.append(
                        d+1 + accumulated_positions[len(accumulated_positions)-1])
            else:
                if len(accumulated_positions) == 0:
                    accumulated_positions.append(1)
                else:
                    accumulated_positions.append(
                        1 + accumulated_positions[len(accumulated_positions)-1])
            previous_bit = pos
            d = 0
    # if the last number is a zero
    if pos == 0:
        if len(accumulated_positions) == 0:
            accumulated_positions.append(d+1)
        else:
            accumulated_positions.append(
                d+1 + accumulated_positions[len(accumulated_positions)-1])
    return accumulated_positions


def solution(A):
    reference_fibs = _generate_sufficient_fibonacci_numbers(100000)

    # accumulated_distances will be in monotonically increasing order
    accumulated_distances = _accumulate_jump_distances(A)

    while
    print(accumulated_distances)
    print(reference_fibs)


solution([0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0])
