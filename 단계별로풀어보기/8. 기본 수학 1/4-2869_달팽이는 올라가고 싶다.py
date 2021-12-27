import math

A, B, V = map(int, input().split())

a = V - B
b = a / (A - B)
print(math.ceil(b))
