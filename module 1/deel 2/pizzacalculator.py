PRIJS_SMALL = 9.99
PRIJS_MEDIUM = 14.99
PRIJS_LARGE = 18.99

AANTAL_SMALL = int(input("Hoeveel Small pizza's wil je bestellen? "))
AANTAL_MEDIUM = int(input("Hoeveel Medium pizza's wil je bestellen? "))
AANTAL_LARGE = int(input("Hoeveel Large pizza's wil je bestellen? "))

TOTAAL_SMALL = AANTAL_SMALL * PRIJS_SMALL
TOTAAL_MEDIUM = AANTAL_MEDIUM * PRIJS_MEDIUM
TOTAAL_LARGE = AANTAL_LARGE * PRIJS_LARGE

TOTAAL_PRIJS = TOTAAL_SMALL + TOTAAL_MEDIUM + TOTAAL_LARGE

print(f"Aantal Small pizza's: {AANTAL_SMALL} - Prijs: ${TOTAAL_SMALL:.2f}")
print(f"Aantal Medium pizza's: {AANTAL_MEDIUM} - Prijs: ${TOTAAL_MEDIUM:.2f}")
print(f"Aantal Large pizza's: {AANTAL_LARGE} - Prijs: ${TOTAAL_LARGE:.2f}")
print("------------------------------------")
print(f"Totaalprijs: ${TOTAAL_PRIJS:.2f}")

