A = []

for _ in range(9):
    A.append(int(input()))

print(max(A))
print(A.index(max(A))+1)

# '맞힌 사람' 답안
a = [int(input()) for _ in range(9)]
print(max(A))
print(A.index(max(A))+1)