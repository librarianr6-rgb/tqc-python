def compute(a, x, y):
    for i in range(y):
        for j in range(x):
            print('%s' %a, end=' ')
        print('')

a = input()
x = eval(input())
y = eval(input())

compute(a, x, y)