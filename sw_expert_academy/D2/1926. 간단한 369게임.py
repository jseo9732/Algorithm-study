N = int(input())

for i in range(1, N+1):
    if "3" in str(i) or "6" in str(i) or "9" in str(i):
        for j in str(i):
            if j in ("3", "6", "9"):
                print("-", end='')
    else:
        print(i, end='')
    print("", end=" ")