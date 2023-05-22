T = int(input())

for i in range(T):
    a = list(map(int, input().split()))
    result = max(a)

    print(f'#{i+1} {result}')

