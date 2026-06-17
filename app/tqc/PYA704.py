n = eval(input())
Set = set()

while n != -9999:
    Set.add(n)
    n = eval(input())

print('Length:', len(Set))
print('Max:', max(Set))
print('Min:', min(Set))
print('Sum:', sum(Set))