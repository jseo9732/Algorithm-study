for _ in range(10):
    t = int(input())
    A, B = map(int, input().split())
    result = 1
    for i in range(B):
        result *= A

    print(f"#{t} {result}")
