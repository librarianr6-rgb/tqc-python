color_dict = {}

while True:    
    key = input("Key: ")
    if key == 'end':
        break        
    value = input("Value: ")
    color_dict[key] = value

Dict = sorted(color_dict)

for row in Dict:
 print("%s: %s" %(row, color_dict[row]))