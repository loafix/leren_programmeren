MIN_GEWICHT = 90
MAX_GEWICHT = 120
MIN_DIEREN_DRESSUUR_ERVARING = 4
MIN_JONGLEREN_ERVARING = 5
MIN_ACROBATIEK_ERVARING = 0  

gewicht = float(input("Wat is uw lichaamsgewicht in kg? "))
vrachtwagen_rijbewijs = input("Bent u in bezit van een geldig Vrachtwagen rijbewijs? (ja/nee) ").lower()
hoge_hoed = input("Heeft u een hoge hoed? (ja/nee) ").lower()

ervaring_dieren_dressuur = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
ervaring_jongleren = int(input("Hoeveel jaar ervaring heeft u met jongleren? "))
ervaring_acrobatiek = int(input("Hoeveel jaar ervaring heeft u met acrobatiek? "))

geschikt = (
    gewicht > MIN_GEWICHT and gewicht < MAX_GEWICHT
    and vrachtwagen_rijbewijs == "ja"
    and hoge_hoed == "ja"
    and (
        ervaring_dieren_dressuur >= MIN_DIEREN_DRESSUUR_ERVARING
        or ervaring_jongleren >= MIN_JONGLEREN_ERVARING
        or ervaring_acrobatiek >= MIN_ACROBATIEK_ERVARING
    )
)

if geschikt:
    print("Gefeliciteerd! U voldoet aan de criteria en mag solliciteren naar de functie van Circusdirecteur voor Circus HotelDeBotel.")
else:
    print("Helaas, u voldoet niet aan alle criteria voor deze functie.")
