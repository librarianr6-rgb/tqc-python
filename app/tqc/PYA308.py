n = eval(input())
for i in range(n):
    temp = num = eval(input())
    ans = 0
    while temp != 0:
        ans += temp % 10
        temp //= 10
    print('Sum of all digits of %d is %d' %(num, ans))