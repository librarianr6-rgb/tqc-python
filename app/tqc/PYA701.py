n = eval(input())
List = []

while n != -9999:
    List.append(n)
    n = eval(input())

Tuple = tuple(List)

print(Tuple)
print('Length:', len(Tuple))
print('Max:', max(Tuple))
print('Min:', min(Tuple))
print('Sum:', sum(Tuple))