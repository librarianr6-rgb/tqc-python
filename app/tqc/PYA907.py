f_name = input()
f_line = f_word = f_char = 0

with open(f_name, 'r') as file: # 或用 file = open(f_name, 'r') 也可以，但最後要 close file 。
    for line in file:
        f_line += 1
        f_word += len(line.split())
        f_char += sum([len(c) for c in line.split()])

print('%d line(s)' %f_line)
print('%d word(s)' %f_word)
print('%d character(s)' %f_char)