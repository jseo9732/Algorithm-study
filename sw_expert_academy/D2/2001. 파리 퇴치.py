T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    array = []
    for _ in range(N):
        array.append(list(map(int, input().split())))

    max = []
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            count = 0
            for k in range(M):
                for l in range(M):
                    count += array[i+k][j+l]
            max.append(count)
    max.sort()
    print(f"#{t} {max[-1]}")