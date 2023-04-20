N, M = map(int, input().split())
array = [i for i in range(1, N+1)]

for _ in range(M):
    i, j, k = map(int, input().split())
    array = array[:i-1] + array[k-1: j] + array[i-1: k-1] + array[j:]

print(" ".join(map(str, array)))
