def compute():
    Dict = {}
    while True:    
        key = input("Key: ")
        if key == 'end':
            return Dict
        value = input("Value: ")
        Dict[key] = value

print('Create dict1:')
dict1 = compute()

print('Create dict2:')
dict2 = compute()

dict1.update(dict2)
dict3 = sorted(dict1)

for row in dict3:
 print("%s: %s" %(row, dict1[row]))