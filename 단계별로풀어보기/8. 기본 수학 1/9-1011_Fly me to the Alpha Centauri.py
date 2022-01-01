T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    length = y - x
    count = 0 # 이동 횟수
    go = 1 # count별 이동 가능한 거리
    go_sum = 0  # 이동한 거리의 합

    while go_sum < length:
        count += 1
        go_sum += go
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            go += 1
    print(count)
