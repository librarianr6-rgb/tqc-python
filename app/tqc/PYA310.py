import math

num = eval(input())
Sum = 0

for n in range(2, num + 1):
    Sum += 1 / (math.sqrt(n - 1) + math.sqrt(n))

print('%.4f' %Sum)