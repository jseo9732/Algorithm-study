b_num = set(range(1, 10001))
a_num = set()

for b in b_num:
    for j in str(b):
        b += int(j)
    a_num.add(b)

aa_num = sorted(b_num - a_num)

for q in aa_num:
    print(q)


