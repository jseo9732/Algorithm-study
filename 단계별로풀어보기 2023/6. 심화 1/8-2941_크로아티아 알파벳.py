# 입력 받은 문자열을 반복문으로 돌면서 같은게 나오면 갯수 체크하는 방식으로 하다가 알파벳에 없는 문자도 있다는 것을 알고
# array를 돌면서 S에 있는 문자면 갯수를 체크하고 나머지를 세려고 했는데 'z=', 'dz='가 여러번 체크되는 문제가 생겨
# '맞힌 사람' 답안을 참고함

array = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
S = input()
cnt = 0
tmp = 0
for i in array:
    cnt += S.count(i)
    print(i, "cnt: ", cnt)
    tmp += S.count(i) * len(i)
    print("tmp: ", tmp)

print(len(S) - tmp + cnt)


# '맞힌 사람' 답안
word = input()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in lst:
    word = word.replace(i, '*')

print(len(word))