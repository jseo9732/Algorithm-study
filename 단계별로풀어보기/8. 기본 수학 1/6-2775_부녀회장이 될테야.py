T = int(input())

for t in range(T):
    k = int(input())  # 층
    n = int(input())  # 호
    before = []
    for i in range(1, n+1):  # 0층 거주자 수 리스트
        before.append(i)
    # print(before)

    for j in range(k):  # 층 수 만큼 반복
        for q in range(1, n):
            before[q] += before[q-1]
        # print(before)  # 프린트문을 추가
    print(before[-1])
