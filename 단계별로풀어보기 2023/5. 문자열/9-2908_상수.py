# A, B = map(list, input().split())
# A.reverse()
# B.reverse()
# reA = int("".join(A))
# reB = int("".join(B))

# print(reA if reA > reB else reB)

# '맞힌 사람' 답안
print(max(input()[::-1].split()))
