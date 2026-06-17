Dict = {}

while True:    
    key = input("Key: ")
    if key == 'end':
        break    
    value = input("Value: ")
    Dict[key] = value

search = input("Search key: ")
print(search in Dict)