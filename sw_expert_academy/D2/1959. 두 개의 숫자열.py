T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max = 0
    long = a if N > M else b
    short = b if N > M else a

    for i in range(len(long)):
        for j in range(len(long)):
            max = log
    # print(f"#{t} {}")