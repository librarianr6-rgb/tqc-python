matrix = []

for i in range(9):
    matrix.append(eval(input()))

largest = max(matrix)
largestIndex1 = matrix.index(largest) // 3
largestIndex2 = matrix.index(largest) % 3

smallest = min(matrix)
smallestIndex1 = matrix.index(smallest) // 3
smallestIndex2 = matrix.index(smallest) % 3

print('Index of the largest number %d is: (%d, %d)' %(largest, largestIndex1, largestIndex2))

print('Index of the smallest number %d is: (%d, %d)' %(smallest, smallestIndex1, smallestIndex2))