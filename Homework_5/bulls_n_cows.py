'''
    Alessia Pizzoccheri - CS 5001 02

    https://stackoverflow.com/questions/6429638/how-to-split-a-string-of-space-separated-numbers-into-integers
'''

from random import randint
from collections import Counter

LENGTH = 4
WIN = 4
ROUNDS = 7

def random_digit():
    '''
        Name: random_digit
        Input: None
        Return: list
    '''

    secret_code = []

    while len(secret_code) != LENGTH:            
        num = randint(0, 9)

        if num not in secret_code:
            secret_code.append(num)    
    
    print(secret_code)
    return secret_code

def player_guess():
    '''
        Name: player_guess
        Input: None
        Return: list
    '''

    while True:

        # player enters guess
        player_guess = str(input('Enter your guess: '))

        # check for spaces in user input
        if ' ' not in player_guess:
            print('Please, separate the digits with spaces.')
        else:
            guess = list(map(int, player_guess.split()))

        # after creating list, make sure all digits are unique    
        unique = len(set(guess)) == len(guess) 
        
        # digits are unique, break out of loop
        if(unique): 
            break
        else :  
            print('Please, only use unique digits.')

    return guess
    

def count_bulls_n_cows(secret_code,guess):
    '''
        Name: bulls_n_cows
        Input: list, list
        Return: dict
    ''' 
    bulls = 0
    cows = 0
    
    # calculate whether it's cows or bulls
    for i in range(len(guess)):
        # cows, digit must be in secret code but at different index
        if guess[i] in secret_code and guess[i] != secret_code[i]:
            cows = cows + 1
        
        # bulls, digit must be in secret code and at same index
        if guess[i] == secret_code[i]:
            bulls = bulls + 1
    
    # created dictionary to return bulls/cows combo
    points = dict()
    points['bulls'] = bulls
    points['cows'] = cows

    return points

def bulls_n_cows(secret_code,guess):
    '''
        Name: bulls_n_cows
        Input: list, list
        Return: dict
    ''' 
    bulls = 0
    cows = 0
    
    # calculate whether it's cows or bulls
    for i in range(len(guess)):
        # cows, digit must be in secret code but at different index
        if guess[i] in secret_code and guess[i] != secret_code[i]:
            cows = cows + 1
        
        # bulls, digit must be in secret code and at same index
        if guess[i] == secret_code[i]:
            bulls = bulls + 1
    
    # created dictionary to return bulls/cows combo
    points = dict()
    points['bulls'] = bulls
    points['cows'] = cows

    return points

def play_bulls_n_cows():
    '''
        Name: play_bulls_n_cows
        Input: int
        Return: None
    ''' 

    counter = 0
    secret_code = random_digit()
    history = []
    guess_history = []

    # play until player wins or player exhausted number of tries
    while True:
        guess = player_guess()
        result = count_bulls_n_cows(secret_code,guess)

        if counter != ROUNDS:

            # if player does not guess
            if guess != secret_code:
                # kepp count of rounds played
                counter = counter + 1

                # create list item with previous guess, round cows and
                # round bulls
                guess_history = [guess,result['cows'],result['bulls']]

                # append item to history list
                history.append(guess_history)

                print('Your guess history:')

                for i in range(len(history)):

                    # format history print 
                    print('Your guess:',history[i][0],'Cows:',history[i][1],
                        'Bulls: ',history[i][2])

            # if player guesses secret code
            else:
                print("You guessed the secret code! YOU WON!")   
                break
        # player does not guess and player runs out of rounds
        else: 
            print('Sorry. You lost! ' +
                'The secret code was',secret_code)
            break