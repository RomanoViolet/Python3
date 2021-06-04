# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    if N <= 0:
        return 0

    bin_string: str = f'{N:b}'
    bit_: int = 0
    size: int = 0
    size_: int = 0

    for bit in bin_string:

        if bit_ == '0' and bit == '1':
            if size > size_:
                size_ = size
            size = 0
        elif bit_ == '1' and bit == '0':
            #bit_ = bit
            size = size + 1
        elif bit_ == '0' and bit == '0':
            size = size + 1
        elif bit_ == '1' and bit == '1':
            pass

        bit_ = bit

    return size_


assert 0 == solution(32), f"32 failed"
assert 5 == solution(1041), f"32 failed"
