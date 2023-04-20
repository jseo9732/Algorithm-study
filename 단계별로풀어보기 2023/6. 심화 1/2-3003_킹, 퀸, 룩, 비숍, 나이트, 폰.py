p = [1, 1, 2, 2, 2, 8]

I = list(map(int, input().split()))

for i in range(len(p)):
    print(p[i] - I[i], end=" ")

