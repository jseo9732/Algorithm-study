for t in range(1, 11):
    N = int(input())
    arr = []
    for _ in range(8):
        arr.append(list(input()))
    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
           if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
               cnt += 1

           s = ""
           for k in range(j, j+N):
               s += arr[k][i]
           if s == s[::-1]:
               cnt += 1
    print(f"#{t} {cnt}")