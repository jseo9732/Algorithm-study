N = int(input())
A = list(map(int, input().split()))
B = []

for i in A:
    B.append(i / max(A) * 100)

print(sum(B)/N)
