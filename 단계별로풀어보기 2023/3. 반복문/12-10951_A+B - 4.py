# import sys

# while True:
#     A, B = map(int, sys.stdin.readline().split())
#     print(A + B)

# 런타임 에러남
# 오류가 발생해도 계속해서 반복하기 때문으로 보임 


# '맞힌 사람' 코드 1
import sys
for line in sys.stdin:
    A,B=map(int,line.split())
    print(A+B)

# readlines() 메서드는 파일 전체를 읽은 뒤, 각 라인을 List에 담아 반환한다. (\n 포함)
# 즉 리스트이기 때문에 for문을 이용하여 파일의 라인 수 만큼만 반복하도록 할 수 있다.

# '맞힌 사람' 코드 2
import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
    except:
        break