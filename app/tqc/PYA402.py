n = eval(input())
List = []

while n != 9999:
    List.append(n)
    n = eval(input())

print(min(List))