T = int(input())
arr = [2, 3, 5, 7, 11]

for t in range(1, T + 1):
    result = [0, 0, 0, 0, 0]
    N = int(input())
    for i in range(len(arr)):
        while N % arr[i] == 0:
            result[i] += 1
            N = N // arr[i]
    print(f"#{t}", end=' ')
    for re in result:
        print(re, end=' ')
    print()