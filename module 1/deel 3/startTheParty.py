gastheer = False
gasten = False
drank = True
chips = False 
gastheer_door = gastheer and drank 
gasten_door = drank and chips


if gastheer_door or gasten_door: 
    print('Start the Party')
else:
    print('No Party')