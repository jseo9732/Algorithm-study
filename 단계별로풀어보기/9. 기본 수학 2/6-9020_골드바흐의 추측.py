def isSosu(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True


T = int(input())

for _ in range(T):
    n = int(input())
    a = int(n/2)
    b = int(n/2)

    for k in range(int(n/2)):
        if isSosu(a) and isSosu(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
