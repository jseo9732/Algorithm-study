# 방법 1
# "맞힌 사람" 답안
# set(집합)이 중복 불가능한 것을 이용한다.
A = set()
for _ in range(10):
    A.add(int(input())%42)

print(len(A))

# 방법 2
# 배열에서 중복되는 값을 제거한다.
A = []
B = []

for i in range(10):
    A.append(int(input()))

for j in A:
    if j % 42 not in B:
        B.append(j % 42)

print(len(B))