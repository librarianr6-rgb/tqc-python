a = eval(input())
b = eval(input())
Sum = 0
List = []

for i in range(a, b + 1):
    if i % 4 == 0 or i % 9 == 0:
        Sum += 1
        List.append(i)
        print('%-4d' %i, end='')
        
        if Sum % 10 == 0:
            print('')

print('\n%d\n%d' %(Sum, sum(List)))