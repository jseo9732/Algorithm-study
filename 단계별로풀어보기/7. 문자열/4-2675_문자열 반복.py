T = int(input())

for q in range(T):
    R, S = input().split()
    P = ""
    for i in S:
        for j in range(int(R)):
            P += i

    print(P)
