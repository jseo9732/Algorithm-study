a = input()
result = ""

for i in a:
    if 65 <= ord(i) <= 90:
        result += i
    elif 97 <= ord(i) <= 122:
        result += chr(ord(i)-32)
    else:
        result += i

print(result)