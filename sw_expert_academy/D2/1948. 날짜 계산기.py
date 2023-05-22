T = int(input())

def month(num):
    if num in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif num == 2:
        return 28
    else:
        return 30


for t in range(1, T + 1):
    result = 0
    m1, d1, m2, d2 = map(int, input().split())
    if m1 == m2:
        result += d2 - d1 + 1
    else:
        result += month(m1) - d1 + 1
        for i in range(m1+1, m2):
            result += month(i)
        result += d2

    print(f"#{t} {result}")