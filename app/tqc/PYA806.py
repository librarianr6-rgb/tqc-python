def compute(Str, s):
    return Str.count(s)

Str = input()
s = input()

print('%s occurs %d time(s)' %(s, compute(Str, s)))