alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

A = input()

for a in alpha:
    if a in A:
        A = A.replace(a, "*")

print(len(A))
