MIN_GEWICHT = 90
MAX_GEWICHT = 120
MIN_DIEREN_DRESSUUR_ERVARING = 4
MIN_JONGLEREN_ERVARING = 5

gewicht = float(input("Wat is uw lichaamsgewicht in kg? "))
vrachtwagen_rijbewijs = input("Bent u in bezit van een geldig Vrachtwagen rijbewijs? (ja/nee) ").lower()
hoge_hoed = input("Heeft u een hoge hoed? (ja/nee) ").lower()

ervaring_dieren_dressuur = int(input("Hoeveel jaar praktijkervaring heeft u met dieren dressuur? "))
ervaring_jongleren = int(input("Hoeveel jaar ervaring heeft u met jongleren? "))

geslacht = input("Wat is uw geslacht? (man/vrouw/anders) ").lower()
afwijzingsredenen = []

geschikt = (gewicht > MIN_GEWICHT and gewicht < MAX_GEWICHT
    and vrachtwagen_rijbewijs == "ja"
    and hoge_hoed == "ja"
    and (ervaring_dieren_dressuur >= MIN_DIEREN_DRESSUUR_ERVARING
        or ervaring_jongleren >= MIN_JONGLEREN_ERVARING))

if gewicht <= MIN_GEWICHT:
    afwijzingsredenen.append("- Gewicht te laag")
if gewicht >= MAX_GEWICHT:
    afwijzingsredenen.append("- Gewicht te hoog")

if vrachtwagen_rijbewijs != "ja":
    afwijzingsredenen.append("- Geen geldig Vrachtwagen rijbewijs")
if hoge_hoed != "ja":
    afwijzingsredenen.append("- Geen hoge hoed")

if geslacht == "man":
    snor = input("Heeft u een snor? (ja/nee) ").lower()
    if snor != "ja":
        afwijzingsredenen.append("- Geen snor")
elif geslacht == "vrouw":
    haarkleur = input("Heeft u rood krulhaar? (ja/nee) ").lower()
    if haarkleur != "ja":
        afwijzingsredenen.append("- Geen rood krulhaar")
else:
    glimlach = input("Heeft u een brede glimlach? (ja/nee) ").lower()
    if glimlach != "ja":
        afwijzingsredenen.append("- Geen brede glimlach")

if geschikt:
    print("Gefeliciteerd! U voldoet aan de criteria en mag solliciteren naar de functie van Circusdirecteur voor Circus HotelDeBotel.")
else:
    print("Helaas, u voldoet niet aan alle criteria voor deze functie.")
    print("Redenen voor afwijzing:")
    for reden in afwijzingsredenen:
        print(reden)
