def compute(x):
    b = True
    if x < 2:
        b = False
    for i in range(2 , x):
        if x % i == 0:
            b = False
            break
    return b

x = eval(input())
if compute(x):
    print('Prime')
else:
    print('Not Prime')