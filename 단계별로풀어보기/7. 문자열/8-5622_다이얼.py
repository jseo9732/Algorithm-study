A = ["ABC", 'DEF', 'GHI', 'JKL', "MNO", 'PQRS', 'TUV', 'WXYZ']
B = input()
time = 0

for b in B:
    num = 2
    for i in A:
        if b in i:
            time += num + 1
        num += 1

print(time)