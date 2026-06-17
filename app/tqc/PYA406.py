cm = eval(input())

while cm != -9999:
    kg = eval(input())
    BMI = kg / (cm / 100) ** 2
    
    print('BMI: %.2f' %BMI)
    
    if BMI >= 30:
        print('State: fat')
    elif BMI >= 25.0:
        print('State: over weight')
    elif BMI >= 18.5:
        print('State: normal')
    else:
        print('State: under weight')
    cm = eval(input())