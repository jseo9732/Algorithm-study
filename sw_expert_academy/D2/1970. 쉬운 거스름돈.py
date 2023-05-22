T = int(input())
m = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(1, T + 1):
    result = [0] * 8
    money = int(input())
    for i in range(8):
        if money // m[i] > 0:
            result[i] = money // m[i]
            money = money % m[i]

    print(f"#{t}")
    for k in result:
        print(k, end=' ')
    print()