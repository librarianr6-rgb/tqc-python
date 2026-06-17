Sum = 0


for i in range(5):
    s = input()
    if s == 'J' or s == 'j':
        Sum += 11
    elif s == 'Q' or s == 'q':
        Sum += 12
    elif s == 'K' or s == 'k':
        Sum += 13
    elif s == 'A' or s == 'a':
        Sum += 1
    else:
        Sum += int(s)

print(Sum)