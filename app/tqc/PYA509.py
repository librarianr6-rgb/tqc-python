import math

def compute(p, q):
    return math.gcd(p, q)

x, y = eval(input())
m, n = eval(input())
p = (x * n + m * y) / compute(x * n + m * y, y * n)
q = (y * n) / compute(x * n + m * y, y * n)

print('%d/%d + %d/%d = %d/%d' %(x, y, m, n, p, q))