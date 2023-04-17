N, M = map(int, input().split())
A = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, input().split())
    temp = A[i-1:j]
    temp.reverse()
    A[i-1:j] = temp

print(" ".join(map(str, A)))