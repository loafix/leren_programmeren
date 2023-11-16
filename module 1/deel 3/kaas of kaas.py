print("Denk aan een kaassoort uit: Emmenthaler, Leerdammer, Parmigiano Reggiano, Goudse Kaas, Blue de Rochbaron, Fouma d'Ambert, Camembert, Mozzarella.")

vraag = input("Is de kaas geel? (ja/nee): ").lower()
if vraag == 'ja':
    vraag2 = input("Zitten er gaten in de kaas? (ja/nee): ").lower()
    if vraag2 == 'ja':
        vraag3 = input('Is de kaas belachelijk duur? (ja/nee): ').lower()
        if vraag3 == 'ja':
            print("Je hebt Emmenthaler in gedachten!")
        else:
            print("Je hebt Leerdammer in gedachten!")
    else:
        vraag4 = input("Is de kaas hard als steen? (ja/nee): ").lower()
        if vraag4 == 'ja':
            print('Je hebt Parmigiano Reggiano in gedachten!')
        else:
            print("Je hebt de Goudse Kaas in gedachten!")
else:
    vraag5 = input("Heeft de kaas blauwe schimmel? (ja/nee): ").lower()
    if vraag5 == 'ja':
        vraag6 = input("Heeft de kaas korst? (ja/nee): ").lower()
        if vraag6 == 'ja':
            print("Je hebt de Blue de Rochbaron in gedachten!")
        else:
            print("Je hebt Fouma d'Ambert in gedachten!")
    else:
        vraag7 = input("Heeft de kaas korst? (ja/nee): ").lower()
        if vraag7 == 'ja':
            print("Je hebt Camembert in gedachten!")
        else:
            print("Je hebt Mozzarella in gedachten!")

print("Bedankt voor het spelen!")

