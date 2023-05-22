import math

T = int(input())

def is_sqrt(num):
    if float(int(math.sqrt(num))) == math.sqrt(num):
        return 0
    else:
        return 1

for t in range(1, T + 1):
    N = int(input())
    tmp = N
    a = 1
    while is_sqrt(tmp):
        a += 1
        tmp = N * a

    print(f"#{t} {a}")