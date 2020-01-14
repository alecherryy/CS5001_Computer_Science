import random
import scrabble_points
from wordlist import get_wordlist

FREQUENCY = {
    'A': 9,
    'B': 2,
    'C': 2,
    'D': 4,
    'E': 12,
    'F': 2,
    'G': 3,
    'H': 2,
    'I': 9,
    'J': 1,
    'K': 1,
    'L': 4,
    'M': 2,
    'N': 6,
    'O': 8,
    'P': 2,
    'Q': 1,
    'R': 6,
    'S': 4,
    'T': 6,
    'U': 4,
    'V': 2,
    'W': 2,
    'X': 1,
    'Y': 2,
    'Z': 1,
    '__': 2
}

POINTS = {
    'A': 1,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 2,
    'H': 4,
    'I': 1,
    'J': 8,
    'K': 5,
    'L': 1,
    'M': 3,
    'N': 1,
    'O': 1,
    'P': 3,
    'Q': 10,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 4,
    'W': 4,
    'X': 8,
    'Y': 4,
    'Z': 10,
}

DRAW = 'D'
WORD = 'W'
PRINT = 'P'
QUIT = 'Q'
ZERO = 0
SEVEN = 0

def create_new_bag(frequency):
    new_bag = scrabble_points.bag_of_letters(frequency)

    return new_bag
    

def draw_letters(new_bag):
    letters_drawn = []
    
    for l in range(7):
        # choose 7 random letters from the bag
        # and append them to a new list
        l = random.choice(new_bag)
        letters_drawn.append(l)
        # remove the 7 random letters from the bag
        new_bag.remove(l)

    return letters_drawn

def draw(bag_of_letters):
    picks = draw_letters(bag_of_letters)
    print('You draw the following letters: ',picks)

    return picks

def print_summary(words_played):
    '''
        Name: print_summary
        Parameters: dict
        Return: str, str 
    '''
    tot = sum(words_played.values())

    # format total points and words played
    message = 'You have a total of',tot,'points\n'
    words = "\n".join("{} -- {} points".format(w, p) for w, p in words_played.items())

    return words, message


def wordgame():
    # new bag of letters
    new_bag = create_new_bag(FREQUENCY)
    wordlist = get_wordlist()
    words_played = {}
    total_points = 0
    
    while True:
        
        # ask for user input
        user_input = input('Pick one of the following:\n'
                + 'D -- Draw 7 letters from the bag \n'
                + 'W -- Make a word from the letters in play \n'
                + 'P -- Print all words played so far \n'
                + 'Q -- Quit \n'
                + 'Your choice: '
                )
        input_uppercase = user_input.upper()

        if input_uppercase == DRAW:
            # check if the bag is empty
            if len(new_bag) > ZERO:
                try: 
                    # pick 7 new letters
                    letters_in_play = draw(new_bag)

                # if the bag is empty, create an exception
                except IndexError:
                    print('The bag is empty! Game over.')
                    break

        elif input_uppercase == WORD:
            # letters the users has
            print(letters_in_play)
            # ask user to create a word
            word = input('Create a word with the letters available to you: ')
            word_upper = word.upper()

            # check if the word exists in the list and if letter is in the 
            # letters at play
            if word_upper in wordlist and [l in word_upper for l in letters_in_play if l in word_upper]:
                
                # calculate points for the round
                total_points = scrabble_points.get_word_value(word_upper,POINTS)
                words_played[word_upper] = total_points
                
                # remove each letter used from the list of letters in play
                for l in word_upper:
                    letters_in_play.remove(l)
            else:
                print('Sorry. The word you chose is not valid')

            # if letters in play is empty, stop the game
            if len(letters_in_play) == ZERO:
                break
            
        elif input_uppercase == PRINT:
            tot = sum(words_played.values())

            print('You have a total of',tot,'points\n')
            print("\n".join("{} -- {} points".format(w, p) for w, p in words_played.items()))

        elif input_uppercase == QUIT:
            print('Bye bye!')
            break
        else:
            print('Please, select a valid choice.')

    print('Thank you for playing!')
wordgame()