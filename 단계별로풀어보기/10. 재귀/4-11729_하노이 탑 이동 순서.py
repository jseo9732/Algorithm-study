def hanoi(N, start, end, a):
    if N == 1:
        print(start, end)
        return
    else:
        hanoi(N-1, start, a, end)
        print(start, end)
        hanoi(N-1, a, end, start)


N = int(input())
print(2**N-1)
hanoi(N, 1, 3, 2)
