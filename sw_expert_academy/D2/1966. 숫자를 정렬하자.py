T = int(input())

for t in range(1, T + 1):
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()

    print(f"#{t}", end=' ')
    for i in S:
        print(i, end=" ")
    print()