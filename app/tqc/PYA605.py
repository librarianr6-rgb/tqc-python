score = []

for i in range(10):
    score.append(eval(input()))

score.sort()
total = sum(score) - score[0] - score[9]

print('%d\n%.2f' %(total, total / 8))