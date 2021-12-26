X = int(input())

line = 0
max_num = 0
while X > max_num:
    line += 1
    max_num += line

gap = max_num - X
if line % 2 == 0:  # 짝수일 때
    top = line - gap  # 분자
    under = gap + 1
else:  # 홀수일 때
    top = gap + 1
    under = line - gap  # 분자

print(f'{top}/{under}')
