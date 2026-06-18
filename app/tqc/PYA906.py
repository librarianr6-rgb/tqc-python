f_name = input()
str_old = input()
str_new = input()


file = open(f_name, 'r+')
datas = file.read()

print("=== Before the replacement")
print(datas)

print("=== After the replacement")
datas = datas.replace(str_old, str_new)
print(datas)

file.seek(0)
file.write(datas)
file.close()