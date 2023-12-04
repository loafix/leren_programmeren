from studieadviestext import *

def vraag_gebruiker(stelling):
    print(stelling)
    print(OPTIES)
    antwoord = int(input())
    return antwoord

def toon_stellingen(weken_gestudeerd):
    antwoorden = []
    for i, stelling in enumerate([
        COMPETENTIE_STELLING_1,
        COMPETENTIE_STELLING_2,
        COMPETENTIE_STELLING_3,
        COMPETENTIE_STELLING_4,
        COMPETENTIE_STELLING_5,
        COMPETENTIE_STELLING_6 if weken_gestudeerd >= 10 else None,
        COMPETENTIE_STELLING_7 if weken_gestudeerd >= 10 else None,
    ]):
        if stelling is None:
            break
        antwoord = vraag_gebruiker(stelling)
        antwoorden.append(antwoord)
    return antwoorden

def geef_advies(antwoorden):
    gemiddelde_score = sum(antwoorden) / len(antwoorden)
    aantal_altijd_vaak = sum(1 for antw in antwoorden if antw <= 1)  # Aantal 'altijd' en 'vaak' antwoorden
    aantal_regelmatig = sum(1 for antw in antwoorden if antw == 2)  # Aantal 'regelmatig' antwoorden
    
    if gemiddelde_score <= 2 or aantal_altijd_vaak > len(antwoorden) / 2:
        print(COMPETENTIE_ADVIES_ZORGELIJK)
    elif gemiddelde_score <= 3 or aantal_altijd_vaak + aantal_regelmatig > len(antwoorden) / 2:
        print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
    else:
        print(COMPETENTIE_ADVIES_GERUSTSTELLEND)

def main():
    print(STUDIEDOKTER_TITEL)
    weken_gestudeerd = int(input(AANTAL_WEKEN_VRAAG))
    antwoorden = toon_stellingen(weken_gestudeerd)
    print(COMPETENTIE_ADVIES_TITEL)
    geef_advies(antwoorden)

if __name__ == "__main__":
    main()