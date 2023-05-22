import math
arr = [200, 180, 160, 140, 120, 100, 80, 60, 40, 20]
score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
T = int(input())

for t in range(1, T + 1):
    result = 0
    N = int(input())
    for _ in range(N):
        x, y = map(int, input().split())
        m = math.sqrt(x*x + y*y)
        for i in range(len(arr)):
            if m > 200:
                continue
            elif m > arr[i]:
                result += score[i-1]
                break

    print(f"#{t} {result}")