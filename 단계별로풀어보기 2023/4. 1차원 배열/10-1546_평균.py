N = int(input())
A = list(map(int, input().split()))
result = []

for i in range(len(A)):
    result.append(A[i]/max(A)*100)

print(sum(result)/N)

# "맞힌 사람" 답안
# 새로 만들 배열의 평균을 내는 것과 원래 배열의 평균에 X100/최대값을 하는 것이 동일하다
print(sum(A)/N * 100/max(A))