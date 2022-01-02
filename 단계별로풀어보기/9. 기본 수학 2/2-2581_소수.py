M = int(input())
N = int(input())

if M == 1:
    M += 1
sosu = [a for a in range(M, N+1)]

for num in range(M, N+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                sosu.remove(num)
                break

if len(sosu) == 0:
    print(-1)
else:
    print(sum(sosu))
    print(min(sosu))
