Nami = Chopper = null = 0

for i in range(5):
    n = eval(input())
    if n == 1:
        Nami += 1
    elif n == 2:
        Chopper += 1
    else:
        null += 1
    
    print('Total votes of No.1: Nami =  %d' %Nami) # 等於後面要有兩個空格。
    print('Total votes of No.2: Chopper =  %d' %Chopper) # 等於後面要有兩個空格。
    print('Total null votes =  %d' %null) # 等於後面要有兩個空格。

if Nami > Chopper:
    print('=> No.1 Nami won the election.')
elif Chopper > Nami:
    print('=> No.2 Chopper won the election.')
else:
    print('=> No one won the election.')