def a(n):
    if(n > 1):
        return n * a(n-1)
    else:
        return 1

N = int(input())
print(a(N))