'''gun beats snake'''
'''snake beats water'''
'''water beats gun'''

import random
while True:
    print('''The Rules:
        gun beats snake
        snake beats water
        water beats gun''')
    a =input('chose "snake" , "water" or "gun": ').lower()
    # b = random.choice('snake','gun','water') # error
    b = random.choice(('snake','gun','water'))

    print(f'''chosen:\nyou = {a}, 
                computer = {b}''')
    if (b=='gun' and a =='snake'):
        print('computer won!\nas gun beats snakes.')
    elif (b=='gun' and a =='water'):
        print('you won!\nas water beats gun.')
    elif (b=='gun' and a =='gun'):
        print('tied.')
    elif (b=='water' and a =='water'):
        print('tied.')
    elif (b=='water' and a =='gun'):
        print('computer won!\nas water beats gun.')
    elif (b=='water' and a =='snake'):
        print('you won!\nas snake beats water.')
    elif (b=='snake' and a =='snake'):
        print('tied.')
    elif (b=='snake' and a =='water'):
        print('computer won!\nas snake beats water')
    elif (b=='snake' and a =='gun'):
        print('you won!as snake beats water')
    else:
        print('snake water and gun only')
    print('____________Finish______________')
    c = input('want to play "again" or "quit": ')
    if c.lower()=='quit':
        break


'''


'''