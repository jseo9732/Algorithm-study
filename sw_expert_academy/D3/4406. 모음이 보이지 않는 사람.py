T = int(input())
arr = ["a", "e", "i", "o", "u"]

for t in range(1, T + 1):
    s = input()
    result = ""
    for i in s:
        if i not in arr:
            result += i
    print(f"#{t} {result}")