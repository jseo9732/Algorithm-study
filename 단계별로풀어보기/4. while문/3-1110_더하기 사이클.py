# 문자열 풀이, 시간초과
# n = input()
# a = n
# count = 0

# while True:
#     if len(a) == 1:
#         a = "0" + a
#     b = str(int(a[0]) + int(a[1]))
#     # print("b: " + b)
#     a = a[-1] + b[-1]
#     # print("a: " + a)
#     count += 1
#     if a == n:
#         print(count)
#         break

# 정수 풀이
n = int(input())
num = n
count = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c

    count += 1
    if n == num:
        print(count)
        break
