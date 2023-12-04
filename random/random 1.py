# lijst = [1, 5, 7, 12]

# print (lijst[3])

# klas = []
# for _ in range (2):
#     persoon = {}
#     persoon['naam'] = input ('wat is uw voornaam? ')
#     persoon['tussenvoegsel'] = input ('wat is uw toegenvoegsel? ')
#     persoon['achternaam'] = input ('wat is uw achternaam? ')
#     persoon ['leeftijd'] = input ('wat is uw leeftijd? ')
#     klas.append(persoon)

# print (klas)
# print (klas[1]['leeftijd'])



auto_lijst = []

for _ in range(5):
    auto = {}
    auto['merk'] = input('Wat is het merk van de auto? ')
    auto['model'] = input('Wat is het model van de auto? ')
    auto['prijs'] = float(input('Wat is de prijs van de auto? '))
    auto_lijst.append(auto)

print("\nPrijzen van de auto's:")
for auto in auto_lijst:
    print(auto['prijs'])
