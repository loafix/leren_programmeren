gastheer = input("Wie is de gastheer?")                   #true/false ->  boolean
gasten = int(input("Hoeveel gasten zijn er? "))
drank = True
chips = True

MijnNaam = "Natalia"
Slber = "Corbijn"
SlberMN = MijnNaam == Slber
gastheer_door =  gastheer and drank
gasten_door = gasten >= 4 and drank and chips
gastheer2 = gastheer == Slber


if (gastheer_door or gasten_door) and not (gastheer2) and gasten <= 20:
    print('Start the Party')
else:
    print('No Party')