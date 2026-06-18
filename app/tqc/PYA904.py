data = []

with open("read.txt","r") as file:
   for line in file:
       print(line)
       data.append(line.split())

name = [data[n][0] for n in range(3)]
height = [eval(data[h][1]) for h in range(3)]
weight = [eval(data[w][2]) for w in range(3)]

print('Average height: %.2f' %(sum(height) / 3))
print('Average weight: %.2f' %(sum(weight) / 3))
print('The tallest is %s with %.2fcm' %(name[height.index(max(height))], max(height)))
print('The heaviest is %s with %.2fkg' %(name[weight.index(max(weight))], max(weight)))