PRIJS_SMALL = 9.99
PRIJS_MEDIUM = 14.99
PRIJS_LARGE = 18.99

aantal_small = int(input("Hoeveel Small pizza's wil je bestellen? "))
aantal_medium = int(input("Hoeveel Medium pizza's wil je bestellen? "))
aantal_large = int(input("Hoeveel Large pizza's wil je bestellen? "))

totaal_small = aantal_small * PRIJS_SMALL
totaal_medium = aantal_medium * PRIJS_MEDIUM
totaal_large = aantal_large * PRIJS_LARGE

totaal_prijs = totaal_small + totaal_medium + totaal_large

print(f"Aantal Small pizza's: {aantal_small} - Prijs: ${totaal_small:.2f}")
print(f"Aantal Medium pizza's: {aantal_medium} - Prijs: ${totaal_medium:.2f}")
print(f"Aantal Large pizza's: {aantal_large} - Prijs: ${totaal_large:.2f}")
print("------------------------------------")
print(f"Totaalprijs: ${totaal_prijs:.2f}")

