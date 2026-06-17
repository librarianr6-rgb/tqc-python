temp = [[], [], [], []]

for i in range(4):
    print("Week %d:" %(i + 1))
    for j in range(3):
        temp[i].append(eval(input("Day %d:" %(j + 1))))
        
Week = []

for k in range(4):
    Week.extend(temp[k])
    
print("Average: %.2f" %(sum(Week) / 12))
print("Highest:", max(Week))
print("Lowest:", min(Week))