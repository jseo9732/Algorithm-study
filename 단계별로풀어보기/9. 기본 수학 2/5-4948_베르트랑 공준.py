def isSosu(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True


all_list = list(range(2, 246912))
sosu_list = []
for i in all_list:
    if isSosu(i):
        sosu_list.append(i)

while 1:
    n = int(input())
    if n == 0:
        break
    ans = 0
    for num in sosu_list:
        if n < num <= 2*n:
            ans += 1
    print(ans)
