T = int(input())

for _ in range(1, T + 1):
    score = [0] * 101
    t = int(input())
    arr = list(map(int, input().split()))
    for i in arr:
        score[i] += 1
    maxIdx = 0
    for j in range(len(score)):
        if score[j] >= score[maxIdx]:
            maxIdx = j

    print(f"#{t} {maxIdx}")