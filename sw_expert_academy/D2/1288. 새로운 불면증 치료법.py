T = int(input())

for t in range(1, T + 1):
    N = int(input())
    result = [0]*10
    mul = 1
    while 0 in result:
        s = str(mul * N)
        mul += 1
        for i in range(len(s)):
            result[int(s[i])] += 1

    print(f"#{t} {s}")
