dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
S = input()
result = 0

for i in S:
    for j in range(len(dial)):
        if i in dial[j]:
            result += j + 3
            
print(result)