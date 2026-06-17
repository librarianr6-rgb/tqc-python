Str = input()
List = Str.split('-')

for i in List:
    if not i.isdigit():
        print('Invalid SSN')
        break
else:
    print('Valid SSN')