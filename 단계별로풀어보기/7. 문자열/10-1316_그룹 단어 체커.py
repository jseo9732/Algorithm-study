N = int(input())
Q = set()
group_word = 0

for i in range(N):
    W = input()
    error = 0
    for w in range(len(W)-1):
        if W[w] != W[w+1]:
            new_W = W[w+1:]
            if new_W.count(W[w]) > 0:
                error += 1

    if error == 0:
        group_word += 1

print(group_word)
