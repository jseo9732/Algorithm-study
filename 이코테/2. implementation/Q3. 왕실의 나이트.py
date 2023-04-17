# 내 답안
# 입력받은 좌표의 인덱스를 구한 뒤 x 또는 y를 if문으로 하나씩 빼거나 더해서 확인해보려다가 비효율적이라 판단하고 포기
point = input()
x = ['a', 'b', 'c', 'd' , 'e', 'f' , 'g', 'h']
y = ['1', '2', '3', '4', '5', '6', '7', '8']
count = 0

px = x.index(point[0])
py = y.index(point[1])

if px - 2 > 0:
    if py - 2 > 0:
        count += 2

    elif py + 2 < 8:
        count += 2

# 교재 답안
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)