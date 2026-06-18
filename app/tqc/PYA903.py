file = open("data.txt", 'a+')

for i in range(5):
    name = input()
    file.write('n' + name)

print("Append completed!")
print('Content of "data.txt":')

file.seek(0)
print(file.read())

file.close()