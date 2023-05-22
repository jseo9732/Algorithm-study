T = int(input())

for t in range(1, T+1):
    s = input()
    result = 1
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            result = 0
    print(f"#{t} {result}")