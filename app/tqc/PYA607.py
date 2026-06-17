List = ['1st', '2nd', '3rd']
score = []

for i in range(3):
    print('The %s student:' %List[i])
    score.append([])
    for j in range(5):
        score[i].append(eval(input()))

for k in range(3):
    print('Student %d' %(k + 1))
    print('#Sum %d' %sum(score[k]))
    print('#Average %.2f' %(sum(score[k]) / 5))