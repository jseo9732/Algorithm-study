# import sys
# N = int(sys.stdin.readline())

# for i in range(1, N+1):
#     for j in range(i):
#         print("*", end="")
#     print()


# '맞힌 사람' 코드
# 굳이 이중 for문을 돌 필요없이 i만큼 "*"을 곱해주어 출력하고 print는 알아서 줄바꿈이 된다.
for i in range(int(input())):
    print("*"*(i+1))