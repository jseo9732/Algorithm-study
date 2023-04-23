S = input().upper()
max_count = 0

for i in range(65, 91):
    count = S.count(chr(i))
    if count > max_count:
        max_count = count
        max_chr = chr(i)
    elif count == max_count:
        max_chr = "?"
    
print(max_chr)
