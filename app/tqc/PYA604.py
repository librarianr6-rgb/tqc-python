List = []
count = [0] * 10

for i in range(10):
    n = eval(input())
    List.append(n)
    count[List.index(n)] += 1

print(List[count.index(max(count))])
print(max(count))