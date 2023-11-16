a = int(input("eerste gehele getal: "))
b = int(input("tweede gehele getal: "))

if a > b:
    Max, Min = a, b
    print(f'a is het grootste getal: {Max}')

elif a < b:
    Max, Min = b, a
    print(f'b is het grootste getal: {Max}')

else:
    print (f'a en b zijn gelijk')