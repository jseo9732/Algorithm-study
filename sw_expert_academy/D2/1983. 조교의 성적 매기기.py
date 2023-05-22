T = int(input())
score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = []
    for i in range(N):
        m, f, h = map(int, input().split())
        arr.append(m*0.35 + f*0.45 + h*0.2)
    aa = arr[K-1]
    arr.sort(reverse=True)

    print(f"#{t} {score[arr.index(aa)//(N//10)]}")