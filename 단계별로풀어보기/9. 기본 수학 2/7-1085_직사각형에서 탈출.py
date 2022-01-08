x, y, w, h = map(int, input().split())

a = x - 0
b = w - x
e = min(a, b)

c = y - 0
d = h - y
f = min(c, d)

print(min(e, f))
