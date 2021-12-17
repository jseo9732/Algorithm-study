C = int(input())

for q in range(C):
    A = list(map(int, input().split()))

    N = A[0]
    sc = A[1:]

    av = sum(sc) / N
    num = 0

    for i in sc:
        if i > av:
            num += 1

    rate = num / N * 100
    print(f'{rate:.3f}%')
