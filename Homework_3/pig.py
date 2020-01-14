''' 
    Alessia Pizzoccheri - CS 5001 02

    A game of PIG.
'''
import random

# CONSTANTS
HOLD = 'H'
ROLL = 'R'
WIN_POINTS = 20
ROLLED_ONE = 'You rolled a 1. You lost all your points!\n'

# randomly generates an int between 1 and 6
def die():
    '''
        Name: die
        Parameter: none
        Return: int
    '''
    die_roll = random.randint(1,6)

    return die_roll

def main():
    # players list with player's name and player's score
    # add player/score pair to the list if you want more
    # than two players  
    players = [
        ['Player One', 0], 
        ['Player Two', 0],
    ]  

    user_win = False

    print('Welcome to PIG! To start playing, get rolling.')

    # play game as long as nobody won
    while user_win == False:
            # for every player in the list, run game()
        for i in range(len(players)):
            # start with Player One 
            if players[0][0] == 'Player One':
                print(players[i][0], "it's your turn.")
                # assign total points for the round to roll variable
                points = 0
                current_round = 0

                while True:
                    # ask player to choose between ROLL and HOLD
                    choice = input(
                        ROLL + ' - Roll\n' +
                        HOLD + ' - Hold\n' +
                        'Your move: ')
                    # convert user input to uppercase
                    choice_format = choice.upper()
                    
                    #  if user chooses ROLL, run die()
                    if choice_format == ROLL:
                        
                        points = die()

                        # if roll is not equal to 1, add roll to 
                        # player's total and go back to ROLL/HOLD
                        if points != 1:
                            current_round += points
                            # print player's points
                            print('You rolled a ', points)
                            # print player's total point for this round
                            print('You collected',current_round,
                            'points this round.')
                            # add points from roll to player's score 
                            players[i][1] += points
                            print(players[i][0],'has collected',players[i][1],'!\n')
                            # if player's total >= to 20, break
                            if players[i][1] >= WIN_POINTS:
                                break
                        # if roll equals 1, reset player's score 
                        # and move to next player
                        else:
                            current_round = 0
                            players[i][1] = 0
                            print(ROLLED_ONE)
                            break
                    #  if user holds, go to next player
                    elif choice_format == HOLD:
                        break
                # if a player wins, end the game
                if players[i][1] >= WIN_POINTS:
                    print(players[i][0].upper(),'WON!\n')
                    # change WIN to True and break while loop
                    user_win = True
                    break
    print('Thank you for playing. Goodbye')
main()
