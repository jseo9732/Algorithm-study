import sys
A, B = map(int, sys.stdin.readline().split())

while A != 0 and B != 0:
    print(A + B)
    A, B = map(int, sys.stdin.readline().split())


# '맞힌 사람' 코드
while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == B == 0:
        break
    print(A + B)
