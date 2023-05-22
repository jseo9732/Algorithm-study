T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = []
    result = 0
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i][j] == 1:
                count += 1
            if arr[i][j] == 0 or j == N - 1:
                if count == K:
                    result += 1
                count = 0
        for k in range(N):
            if arr[k][i] == 1:
                count += 1
            if arr[k][i] == 0 or k == N - 1:
                if count == K:
                    result += 1
                count = 0
    print(f"#{t} {result}")