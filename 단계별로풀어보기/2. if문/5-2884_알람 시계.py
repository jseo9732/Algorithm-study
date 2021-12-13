H, M = map(int, input().split())

if M >= 45:
    print(H, M-45)
elif M < 45:
    q = M - 45
    if H == 0:
        print(23, 60 - abs(q))
    elif H != 0:
        print(H-1, 60 - abs(q))
