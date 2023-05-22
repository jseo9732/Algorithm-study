T = int(input())

for t in range(1, T + 1):
    L, U, X = map(int, input().split())
    result = 0
    if L > X:
        result = L - X
    elif U < X:
        result = -1
    else:
        result = 0

    print(f"#{t} {result}")