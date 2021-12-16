A = int(input())
B = int(input())
C = int(input())

q = A * B * C

for i in range(10):
    num = 0
    for j in str(q):
        if str(i) == j:
            num += 1
    print(num)
