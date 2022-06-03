import random     
def game():

    alist = ['rock','paper','scissors']

    player = input('pick:')

    CPU = random.choice(alist)

    while player not in alist:

        print('ERROR')

        player = input('pick again:')

    else:

        print(f'player({player}):CPU({CPU})')

        if player == 'rock' and CPU == 'scissors':

            print('player is the winner')

        elif player == 'rock' and CPU == 'paper':

            print('CPU is the winner')

        elif player == 'paper' and CPU == 'scissors':

            print('CPU is the winner')

        elif player == 'scissors' and CPU == 'rock':

            print('CPU is the winner')

        elif player == 'scissors' and CPU == 'paper':

            print('player is the winner')

        elif player == 'paper' and CPU == 'rock':

            print('player is the winner')

        elif player == CPU:

            print('its a tie')

            game()
game()

