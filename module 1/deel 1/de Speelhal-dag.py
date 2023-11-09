aantal_personen = 1
kosten_per_ticket = 7.42
tijd_in_minuten = 10
kosten_per_5_minuten = 0.41
totale_kosten_tickets = aantal_personen * kosten_per_ticket
aantal_blokken = tijd_in_minuten / 5
totale_kosten_vr_seat = aantal_personen * kosten_per_5_minuten * aantal_blokken
te_betalen_bedrag = totale_kosten_tickets + totale_kosten_vr_seat

print(f"Kosten toegangstickets: {totale_kosten_tickets:.2f} euro")
print(f"Kosten VIP-VR-GameSeat: {totale_kosten_vr_seat:.2f} euro")
print(f"Totaal te betalen bedrag: {te_betalen_bedrag:.2f} euro")
print (f"Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met {tijd_in_minuten} VR kost je maar {te_betalen_bedrag}")