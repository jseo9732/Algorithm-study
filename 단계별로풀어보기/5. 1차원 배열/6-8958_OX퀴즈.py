N = int(input())
final = 0

for i in range(N):
    an = input()
    sc = 0
    for j in an:
        if j == "O":
            sc += 1
            final += sc
        else:
            sc = 0

    print(final)
    final = 0
