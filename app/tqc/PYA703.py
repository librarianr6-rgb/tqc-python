Str = input()
List = []

while Str != 'end':
    List.append(Str)
    Str = input()

Tuple = tuple(List)

print(Tuple)
print(Tuple[0:3])
print(Tuple[len(Tuple) - 3:len(Tuple)])