N = int(input())
start = 1
sum_six = 6
count = 1

while N > start:
    count += 1
    start += sum_six
    sum_six += 6

print(count)
