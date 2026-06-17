def compute(x, y):
    if y == 0:
        return x
    else:
        return compute(y, x % y) # 或者直接用 math 套件的 gcd 方法也行。

x, y = eval(input())

print(compute(x, y))