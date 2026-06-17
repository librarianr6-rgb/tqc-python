Str = input()
List = [int(i) for i in Str.split(' ')]

print('Total = %d' %sum(List))
print('Average = %.1f' %(sum(List) / len(List)))