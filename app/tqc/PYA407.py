year = eval(input())

while year != -9999:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('%d is a leap year.' %year)
    else:
        print('%d is not a leap year.' %year)
    year = eval(input())