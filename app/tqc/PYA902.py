f = open("read.txt", 'r')
data = f.read()
f.close()

List = [int(i) for i in data.split(' ')]
print(sum(List))