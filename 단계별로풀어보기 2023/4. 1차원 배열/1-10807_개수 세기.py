N = int(input())
A = list(map(int, input().split()))
v = int(input())
count = 0

for i in A:
    if i == v:
        count += 1

print(count)

# '맞힌 사람' 코드
print(A.count(v))