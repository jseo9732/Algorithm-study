N, K = map(int, input().split())
cnt = 0

while True:
    if N % K == 0:
        N = N // K
        print("나누기: ", N)
    else:
        N -= 1
        print("빼기: ", N)
    cnt = cnt + 1
    print(cnt)
    if N == 1:
        break

print(cnt)

# 교재 답안
# N, K을 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)