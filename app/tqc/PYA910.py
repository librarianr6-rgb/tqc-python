f_name = "read.dat"
male = female = 0

with open(f_name, 'rb') as f:
    for line in f:        
        print(line.decode('utf-8'))        
        if line.decode('utf-8').split()[2] == '0':
            female += 1
        elif line.decode('utf-8').split()[2] == '1':
            male += 1        

print('Number of males: %d' %male)
print('Number of females: %d' %female)