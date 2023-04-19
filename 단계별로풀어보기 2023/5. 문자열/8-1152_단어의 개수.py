print(len(list(input().split())))

# '맞힌 사람' 답안
# 내가 한 답안은 배열을 사용했기 때문에
# 문자열을 이용해서 푸는 방법
S = input().strip()
print(S.count(" ")+1 if S else 0)