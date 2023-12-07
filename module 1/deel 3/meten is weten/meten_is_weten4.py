a = int(input("eerste gehele getal: "))
b = int(input("tweede gehele getal: "))

if a > b:
    Max = b
    print(f'a is het grootste getal: {Max}')

elif a < b:
    Min = b
    print(f'b is het grootste getal: {Min}')

else:
    print (f'a en b zijn gelijk')

if Max is None:
    Max = b
else:
    Min = b

