T = int(input())

for t in range(1, T + 1):
    S =""
    N = int(input())
    for _ in range(N):
        C, K = input().split()
        S += C*int(K)
    print(f"#{t}")
    for i in range(1, len(S)):
        if i % 10 == 0:
            print(S[i - 1], end='')
            print()
        else:
            print(S[i-1], end='')
    print(S[-1])
