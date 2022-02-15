N, M = map(int, input().split())
board = []
count = []

for _ in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i, i+8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:  # 짝수일때
                    if board[k][l] != 'W':
                        first_W += 1
                    if board[k][l] != 'B':
                        first_B += 1
                else:  # 홀수일때
                    if board[k][l] != 'B':
                        first_W += 1
                    if board[k][l] != 'W':
                        first_B += 1
        count.append(min(first_W, first_B))
print(min(count))
