N, M = map(int, input().split())
A = [str(i+1) for i in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    a = A[i-1]
    A[i-1] = A[j-1]
    A[j-1] = a

print(" ".join(A))

# '맞힌 사람' 답안
N, M = map(int, input().split())
buckets = list(range(1, N+1))

for _ in range(M):
  a, b = map(int, input().split())
  buckets[a-1], buckets[b-1] = buckets[b-1], buckets[a-1]
print(' '.join(map(str, buckets)))