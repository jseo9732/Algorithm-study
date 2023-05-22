T = int(input())

for i in range(T):
    a = input()
    M = int(a[4:6])
    D = int(a[6:8])
    result = a[0:4] + "/" + a[4:6] + "/" + a[6:8]
    if M in (1, 3, 5, 7, 8, 10, 12):
        if D < 1 or D > 31:
            result = -1

    elif M in (4, 6, 9, 11):
        if D < 1 or D > 30:
            result = -1

    elif M == 2:
        if D < 1 or D > 28:
            result = -1

    else:
        result = -1

    print(f'#{i+1} {result}')