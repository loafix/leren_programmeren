PRIJS_SMALL = 9.99
PRIJS_MEDIUM = 14.99
PRIJS_LARGE = 18.99

print("Kies het formaat van de pizza:")
print("1. Small")
print("2. Medium")
print("3. Large")

keuze = int(input("Voer het nummer in van het gewenste formaat: "))

if keuze == 1:
    formaat = "Small"
    prijs = PRIJS_SMALL
elif keuze == 2:
    formaat = "Medium"
    prijs = PRIJS_MEDIUM
elif keuze == 3:
    formaat = "Large"
    prijs = PRIJS_LARGE
else:
    print("Ongeldige keuze. Kies 1, 2 of 3 voor Small, Medium of Large.")
    exit()

aantal = int(input(f"Hoeveel {formaat} pizza's wil je bestellen? "))

totaal_prijs = aantal * prijs

print("********** PIZZA BONNETJE **********")
print(f"Aantal {formaat} pizza's: {aantal} - Prijs: ${totaal_prijs:.2f}")
print("------------------------------------")
print(f"Totaalprijs: ${totaal_prijs:.2f}")
print("************************************")
