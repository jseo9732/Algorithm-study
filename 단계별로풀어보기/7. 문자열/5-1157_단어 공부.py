from abc import ABC


A = input().upper()
dic = {}

for i in A:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

# print(dic)
# print(max(dic, key=dic.get))

sorted_dict = sorted(dic.items(), key=lambda item: item[1], reverse=True)

# print(sorted_dict)

if len(dic) >= 2:
    if sorted_dict[0][1] == sorted_dict[1][1]:
        print("?")
    else:
        print(max(dic, key=dic.get))
else:
    print(max(dic, key=dic.get))
