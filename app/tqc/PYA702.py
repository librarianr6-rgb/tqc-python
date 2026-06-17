List1 = []

print("Create tuple1:")
n = eval(input())

while n != -9999:
    List1.append(n)
    n = eval(input())
Tuple1 = tuple(List1)

List2 = []

print("Create tuple2:")
n = eval(input())

while n != -9999:
    List2.append(n)
    n = eval(input())
Tuple2 = tuple(List2)

List1.extend(List2)
Tuple = tuple(List1)
List1.sort()

print('Combined tuple before sorting:', Tuple)
print('Combined list after sorting:', List1)