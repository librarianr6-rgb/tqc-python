f_name = input()
n = int(input())
countDict = {}
f_word = []

with open(f_name, 'r') as file:
    for line in file:
        for w in line.split():
            if w in countDict:
                countDict[w] += 1
            else:
                countDict[w] = 1

for word in countDict:
    if countDict[word] == n:
        f_word.append(word)

f_word.sort()

for ans in f_word:
    print(ans)