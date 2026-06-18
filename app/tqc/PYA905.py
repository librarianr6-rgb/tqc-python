f_name = input()
string = input()

file = open(f_name, 'r+')
datas = file.read()

print("=== Before the deletion")
print(datas)

print("=== After the deletion")
datas = datas.replace(string, '')
print(datas)

file.seek(0)
file.write(datas)
file.close()