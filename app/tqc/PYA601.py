Sum = 0
List = []

for i in range(12):
    List.append(eval(input()))
    if i % 2 == 0:
        Sum += List[i]

for j in range(4):
    print('%3d%3d%3d' %(List[j * 3], List[j * 3 + 1], List[j * 3 + 2]))

print(Sum)