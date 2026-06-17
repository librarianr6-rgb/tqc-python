matrix1 = [[], []]
matrix2 = [[], []]

print("Enter matrix 1:")

for i in range(2):
    for j in range(2):                
        print("[%d, %d]: " % (i+1, j+1), end = '')
        matrix1[i].append(eval(input()))    

print("Enter matrix 2:")

for i in range(2):
    for j in range(2):        
        print("[%d, %d]: " % (i+1, j+1), end = '')
        matrix2[i].append(eval(input()))

print("Matrix 1:")
for i in range(2):
    for j in range(2):
        print('%d ' %matrix1[i][j], end='') # 不用輸出 * 號。
    print('')

print("Matrix 2:")
for i in range(2):
    for j in range(2):
        print('%d ' %matrix2[i][j], end='')
    print('')

print("Sum of 2 matrices:")
for i in range(2):
    for j in range(2):
        print('%d ' %(matrix1[i][j] + matrix2[i][j]), end='')
    print('')