A = []
B = []

for i in range(10):
    A.append(int(input()))

for j in A:
    if j % 42 not in B:
        B.append(j % 42)

print(len(B))
