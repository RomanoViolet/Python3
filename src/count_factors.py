def solution(N):
    i = 1
    ndivisors = 0
    #divisors = list()
    if N == 1:
        return 1
    while (i * i <= N):
        if N % i == 0:
            if N / i != i:
                ndivisors += 2
                #divisors.append(i, )
                # divisors.append(N/i)

            else:
                ndivisors += 1
                # divisors.append(i)
        i += 1
    #print(f"All divisors: { divisors }")
    return ndivisors


#assert 8 == solution(24)
#assert 1 == solution(1)
#assert 2 == solution(2)
#assert 5 == solution(16)
#assert 9 == solution(36)
#assert 4 == solution(69)
assert 16 == solution(120)
