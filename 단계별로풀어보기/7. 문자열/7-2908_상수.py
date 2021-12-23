A = list(input().split())
B = []
a = ""

for i in A:
    for j in range(2, -1, -1):
        a += i[j]
    B.append(a)
    a = ""

print(max(B))
