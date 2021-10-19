import game

selection = '0'
while selection != '5':
    print('1. New game')
    print('2. View ships')
    print('3. Make a guess')
    print('4. View guesses')
    print('5. Exit')

    selection = input('Choose option 1 - 5: ')

    if selection == '1':
        b = int(input('Battleship position: '))
        s = int(input('Submarine position: '))
        d = int(input('Destroyer position: '))   
           
        game.start_new(b, s, d)

    elif selection == '2':
        s = game.get_ships()
        print(f'Ships: {s}')

    elif selection == '3':
        p = int(input('Guess position: '))
        result = game.make_guess(p)
        print(f'You: {result}')

    elif selection == '4':
        g = game.get_guesses()
        print(f'Guesses: {g}')
    
