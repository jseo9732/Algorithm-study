# N = int(input())
# result = 0

# for _ in range(N):
#     S = input()
#     print(S.find)

# 블로그 답안
N = int(input())
result = N

for _ in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            continue
        elif word[j] in word[j+1: ]:
            result -= 1
            break

print(result)

