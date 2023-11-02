aantal_croissantjes = 17
prijs_per_croissantje = 0.39

aantal_stokbroden = 2
prijs_per_stokbrood = 2.78

aantal_kortingsbonnen = 3
waarde_kortingsbon = 0.50

kosten_croissantjes = aantal_croissantjes * prijs_per_croissantje

kosten_stokbroden = aantal_stokbroden * prijs_per_stokbrood

totale_kosten_zonder_korting = kosten_croissantjes + kosten_stokbroden

korting = aantal_kortingsbonnen * waarde_kortingsbon

te_betalen_bedrag = totale_kosten_zonder_korting - korting

print(f"Kosten croissantjes: {kosten_croissantjes:.2f} euro")
print(f"Kosten stokbroden: {kosten_stokbroden:.2f} euro")
print(f"Totale kosten zonder korting: {totale_kosten_zonder_korting:.2f} euro")
print(f"Korting: {korting:.2f} euro")
print(f"Te betalen bedrag: {te_betalen_bedrag:.2f} euro")
print (f'De feestlunch kost je bij de bakker {te_betalen_bedrag} euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')