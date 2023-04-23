C = int(input())

for _ in range(C):
    array = list(map(int, input().split()))
    avg = sum(array[1:])/array[0]
    cnt = 0
    for i in array[1:]:
        if i > avg:
            cnt += 1
    print(f'{cnt/array[0]*100:.3f}%')