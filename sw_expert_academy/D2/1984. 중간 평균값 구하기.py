T = int(input())

for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    arr.sort()
    print(f"#{t} {round(sum(arr[1:9]) / 8)}")
