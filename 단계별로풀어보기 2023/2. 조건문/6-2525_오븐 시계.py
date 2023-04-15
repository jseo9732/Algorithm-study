import sys
A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

total = A * 60 + B + C
if(total >= 24 * 60):
    total -= 24 * 60

print(total // 60, total % 60)