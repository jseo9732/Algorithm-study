import sys

a, b, c = sys.stdin.readline().split()
A = int(a)
B = int(b)
C = int(c)

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)