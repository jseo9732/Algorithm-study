T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    result = ""
    if a > b:
        result += ">"
    elif a < b:
        result += "<"
    else:
        result += "="

    print(f'#{i+1} {result}')