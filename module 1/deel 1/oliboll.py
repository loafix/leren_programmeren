oliebol_prijs = 99
prijs_10_oliebollen = 750 
appelflap_prijs = 149

antaal_oliebollen = 11
antaal_appelflappen = 0

antaal_zakken = antaal_oliebollen //10
antaal_lossen = antaal_oliebollen %10
oliebollen_totaal = antaal_zakken * prijs_10_oliebollen + antaal_lossen * oliebol_prijs

prijs_totaal = antaal_oliebollen * oliebol_prijs + antaal_appelflappen * appelflap_prijs
totaal_eur = prijs_totaal/100
print(f"De {antaal_oliebollen} oliebollen en {antaal_appelflappen} appeleflappen kosten samen: {totaal_eur}")
