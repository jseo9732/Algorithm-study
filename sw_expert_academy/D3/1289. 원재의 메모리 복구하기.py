T = int(input())

for t in range(1, T + 1):
    a = input()
    result = ["0"] * len(a)
    cnt = 0

    for i in range(len(a)):
        if a[i] == result[i]:
            continue
        else:
            for j in range(i, len(a)):
                result[j] = a[i]
            cnt += 1
    print(f"#{t} {cnt}")