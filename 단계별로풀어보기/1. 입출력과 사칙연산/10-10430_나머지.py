A, B, C = input().split()

print((int(A)+int(B)) % int(C))
print(((int(A) % int(C)) + (int(B) % int(C))) % int(C))
print((int(A)*int(B)) % int(C))
print(((int(A) % int(C)) * (int(B) % int(C))) % int(C))


A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
print((A+B) % C)
print(((A % C) + (B % C)) % C)
print((A*B) % C)
print(((A % C) * (B % C)) % C)
