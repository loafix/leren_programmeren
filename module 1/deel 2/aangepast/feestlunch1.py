aantal_croissantjes = int(input("Hoeveel croissantjes wil je bestellen? "))
PRIJS_PER_CROISSANTJE = 39

aantal_stokbroden = int(input("Hoeveel stokbroden wil je bestellen? "))
PRIJS_PER_STOLBROOD = 278

aantal_kortingsbonnen = int(input("Hoeveel kortingsbonnen heb je? "))
WAARDE_KORTINGSBON = 50

kosten_croissantjes = aantal_croissantjes * PRIJS_PER_CROISSANTJE
kosten_stokbroden = aantal_stokbroden * PRIJS_PER_STOLBROOD
totale_kosten_zonder_korting = kosten_croissantjes + kosten_stokbroden
korting = aantal_kortingsbonnen * WAARDE_KORTINGSBON
te_betalen_bedrag = totale_kosten_zonder_korting - korting

kosten_croissantjes /= 100
kosten_croissantjes /= 100
te_betalen_bedrag /= 100

print(f"Kosten croissantjes: {kosten_croissantjes} euro")
print(f"Kosten stokbroden: {kosten_stokbroden} euro")
print(f"Totale kosten zonder korting: {totale_kosten_zonder_korting} euro")
print(f"Korting: {korting} cent")
print(f"Te betalen bedrag: {te_betalen_bedrag} euro")
print(f'De feestlunch kost je bij de bakker {te_betalen_bedrag} euro voor de {aantal_croissantjes} croissantjes en de {aantal_stokbroden} stokbroden als de {aantal_kortingsbonnen} kortingsbonnen nog geldig zijn!')
