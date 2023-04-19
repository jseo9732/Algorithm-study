S = input()

for i in range(97, 123):
    try:
        print(S.index(chr(i)), end=' ')
    except ValueError:
        print(-1, end=' ')

# '맞힌 사람' 답안
for i in range(97,123):
    print(S.find(chr(i)), end=' ')