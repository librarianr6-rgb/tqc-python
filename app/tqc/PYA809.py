Str = input()

if len(Str) <= 7 or Str.islower() or Str.isdigit() or not Str.isalnum():
    print('Invalid password')
else:
    print('Valid password')