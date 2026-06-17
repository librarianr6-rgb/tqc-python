Str = input()
Sum = 0

for i in range(len(Str)):
    print("ASCII code for '%s' is %d" %(Str[i], ord(Str[i])))
    Sum += ord(Str[i])

print(Sum)