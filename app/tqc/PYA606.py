def compute(lst):    
    for row in range(rows):
        for col in range(cols):
            print('%4d' %lst[row][col], end='')
        print('')

rows = eval(input())
cols = eval(input())
lst = []

for row in range(rows):
    lst.append([])
    for col in range(cols):
        lst[row].append(col - row)

compute(lst)