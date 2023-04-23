lst = ["F", "D", "C", "B", "A"]
sum = 0
numSum = 0

for _ in range(20):
    subject, num, score = input().split()
    if score == 'P':
        # numSum += int(num[0])
        continue
    elif score == "F":
        score = lst.index(score[0])
        numSum += int(num[0])
    else:
        score = lst.index(score[0]) + (0.5 if score[1] == "+" else 0)
        numSum += int(num[0])
        sum += (score * int(num[0]))

print(f'{sum / numSum:.6f}')