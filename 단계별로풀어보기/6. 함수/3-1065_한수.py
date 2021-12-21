n = int(input())


def hhhh(n):
    if n < 100:
        hansu = n
    else:
        hansu = 99
        for i in range(100, n+1):
            A = list(map(int, str(i)))
            if A[0] - A[1] == A[1] - A[2]:
                hansu += 1

    print(hansu)


hhhh(n)
