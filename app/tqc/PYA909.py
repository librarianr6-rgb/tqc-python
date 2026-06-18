f_name = "data.dat"
file = open(f_name, 'wb')

for i in range(5):    
    file.write((input() + 'n').encode('utf-8'))

print('The content of "data.dat":')

with open(f_name, 'rb') as file:
    # print(file.read().decode('utf-8'))
    for line in file:
        print(line.decode('utf-8'))