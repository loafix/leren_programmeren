aantal_personen = int(input("Hoeveel personen gaan naar de speelhal? "))
KOSTEN_PER_TICKET = 742
tijd_in_minuten = int(input("Hoeveel minuten ga je de VR-GameSeat gebruiken? "))
KOSTEN_PER_5_MINUTEN = 41

totale_kosten_tickets = aantal_personen * KOSTEN_PER_TICKET
aantal_blokken = tijd_in_minuten / 5
TOTALE_KOSTEN_VR_SEAT = aantal_personen * KOSTEN_PER_5_MINUTEN * aantal_blokken
te_betalen_bedrag = totale_kosten_tickets + TOTALE_KOSTEN_VR_SEAT

totale_kosten_tickets /= 100
TOTALE_KOSTEN_VR_SEAT /= 100
te_betalen_bedrag /= 100

print(f"Kosten toegangstickets: {totale_kosten_tickets} euro")
print(f"Kosten VIP-VR-GameSeat: {TOTALE_KOSTEN_VR_SEAT} euro")
print(f"Totaal te betalen bedrag: {te_betalen_bedrag} euro")
print(f"Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met {tijd_in_minuten} VR kost je maar {te_betalen_bedrag} euro")
