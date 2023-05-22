T = int(input())

for t in range(1, T + 1):
    a, b, c, d = map(int, input().split())
    h = a + c
    m = b + d
    if h > 12:
        h -= 12
    h += m // 60
    m = m % 60
    print(f"#{t} {h} {m}")