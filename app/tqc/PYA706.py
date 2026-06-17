k = eval(input())

for i in range(k):
    Str = input()
    check = set(Str.lower())
    check.remove(' ')
    print(len(check) == 26)