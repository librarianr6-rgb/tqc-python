a = eval(input())
b = eval(input())
Sum = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        Sum += i

print(Sum)