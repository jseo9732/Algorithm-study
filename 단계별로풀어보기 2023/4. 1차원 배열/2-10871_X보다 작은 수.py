N, X = map(int, input().split())
A = list(map(int, input().split()))
count = 0

for i in A:
    if i < X:
        print(i, end=" ")

# '맞힌 사람' 답안
n, x = map(int, input().split())
answer = ' '.join([i for i in input().split() if int(i) < x])
print(answer)