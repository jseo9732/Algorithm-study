T = int(input())

for i in range(T):
    A = list(map(int, input().split()))
    result = sum(A)/10

    print(f'#{i+1} {round(result)}')