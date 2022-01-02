N = int(input())
num = list(map(int, input().split()))

if 1 in num:
    num.remove(1)

for i in range(2, max(num)):
    for j in num:
        # print(j, i)
        if j > i and j % i == 0:
            # print(j)
            num.remove(j)
print(len(num))
