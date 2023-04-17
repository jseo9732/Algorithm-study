A = []

for _ in range(28):
    A.append(int(input()))

for i in range(1, 31):
    if i not in A:
        print(i)

# '맞힌 사람' 답안
x= list(map(int,range(1,31)))
for i in range(28):
    x.remove(int(input()))
for j in x:
    print(j)