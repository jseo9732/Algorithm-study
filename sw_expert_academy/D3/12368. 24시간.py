T = int(input())

for t in range(1, T + 1):
    A, B = map(int, input().split())
    print(f"#{t} {A + B - 24 if A + B >= 24 else A + B}")