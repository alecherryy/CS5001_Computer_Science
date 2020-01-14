''' 
    Alessia Pizzoccheri - CS 5001 02

    This is a Morse Code Application. Users are asked to input an 
    alphanumeric phrase into prompter and they will be provided with the translation 
    into Morse Code. If the user inputs an invalid character, s/he is notified of
    her/his mistake and asked to enter a new phrase. Entering :q: will cause the
    script to stop running
'''

CODE_LIST = [
    [' ', '/'], 
    ['A', '.-'], 
    ['B', '-...'],
    ['C', '-.-.'], 
    ['D', '-..'], 
    ['E', '.'],
    ['F', '..-.'], 
    ['G', '--.'], 
    ['H', '....'], 
    ['I', '..'], 
    ['J', '.---'],
    ['K', '-.-'], 
    ['L', '.-..'], 
    ['M', '--'], 
    ['N', '-.'], 
    ['O', '---'],
    ['P', '.--.'], 
    ['Q', '--.-'], 
    ['R', '.-.'], 
    ['S', '...'], 
    ['T', '-'],
    ['U', '..-'], 
    ['V', '...-'], 
    ['W', '.--'], 
    ['X', '-..-'], 
    ['Y', '-.--'],
    ['Z', '--..'], 
    ['0', '-----'], 
    ['1', '.----'], 
    ['2', '..---'], 
    ['3', '...--'],
    ['4', '....-'], 
    ['5', '.....'], 
    ['6', '-....'], 
    ['7', '--...'],
    ['8', '---..'], 
    ['9', '----.'], 
    ['?', '..--..'], 
    ['!', '-.-.--'], 
    ['\'', '.----.'], 
    ['"', '.-..-.'], 
    [',', '--..--'],
]

# index of items inside CODE_LIST paira
CODE_LETTER = 0
CODE_SEQUENCE = 1

# invalid character
INVALID_CHAR = ''

# escape character
ESCAPE_CHAR = ':q:'

# function to check a single character against CODE_LIST
def check_char(char):
    '''
        Name: check_char
        Parameter: str
        Return: str
    '''
    # conver function parameter into uppercase character
    char_upper = char.upper()
    # empty variable used to check whether or not the character is valid
    valid_char = INVALID_CHAR

    # run upper_char against characters inside CODE_LIST
    for i in range(len(CODE_LIST)): 
        # if match, assign respective morse code to valid_char
        if char_upper == CODE_LIST[i][CODE_LETTER]:
            valid_char = CODE_LIST[i][CODE_SEQUENCE]
    
    return valid_char

def main():
    '''
        Test Case #1
            Hello, world!
            .... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--
        Test Case #2
            Andiamo a cena
            .- -. -.. .. .- -- --- / .- / -.-. . -. .-
        Test Case #3
            email@address.com
            One of the characters you entered is invalid. Please choose a different phrase
    '''
    # welcome message
    print('Welcome to Morse Code Application. Enter your alphanumeric message and ' +
    'I will convert it into a morse code message. To kill the application user the' +
    ' :q: escape character.')
    
    # run the app unless the user enter :q:
    while True:
        # ask user to enter a phrase
        phrase = input('Enter a phrase: ')

        # if user enters escape character, kill the app
        if phrase == ESCAPE_CHAR:
            break

        morse_list = []
        # variable to check whether or not the user entered a valid phrase
        is_valid = True
        # run check_char for each character in the phrase 
        for j in range(len(phrase)):
            # if character is valid, append it to the morse_list empty list
            if check_char(phrase[j]) != INVALID_CHAR:
                add_char = check_char(phrase[j])
                morse_list.append(add_char)
            # if the character is NOT valid, change is_valid to false
            else:
                is_valid = False
        # if is_valid equals True, convert list of morse codes into a string
        # and print it 
        if is_valid:
            morse_code = ' '
            morse_final = morse_code.join(morse_list)
            print('Your Morse code: ', morse_final)
        # if is_valid equals False, alert user they entered an invalid character
        else:
            print('One of the characters you entered is invalid.' + 
            ' Please choose a different phrase.')
    # farewell to the user
    print('Goodbye!')
main()

