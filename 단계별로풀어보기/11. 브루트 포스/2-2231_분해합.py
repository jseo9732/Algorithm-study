N = int(input())
result = 0

for i in range(1, N+1):
    A = list(map(int, str(i)))
    S = i + sum(A)
    if (S == N):
        result = i
        break

print(result)
