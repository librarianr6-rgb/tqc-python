k = eval(input())


for i in range(k):
    Str = input()
    List = [float(i) for i in Str.split(' ')]
    print('%.2f' %(max(List) - min(List)))