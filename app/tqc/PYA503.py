def compute(a, b):
    Sum = 0
    for i in range(a, b + 1):
        Sum += i
    return Sum

a = eval(input())
b = eval(input())

print(compute(a, b))