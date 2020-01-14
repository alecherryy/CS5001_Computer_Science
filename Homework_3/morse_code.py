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

# user options
OPTION_A = 'A'
OPTION_B = 'B'
OPTION_C = 'C'
# index of items inside CODE_LIST paira
CODE_LETTER = 0
CODE_SEQUENCE = 1
# invalid character
INVALID_CHAR = ''
# escape character
ESCAPE_CHAR = ':q:'

# function to check user input against CODE_LIST
def check(value,check,output):
    '''
        Name: check
        Parameter: str, int, int
        Return: str
    '''

    # empty variable used to check whether or not the character is valid
    valid_value = INVALID_CHAR

    # check value_up against characters inside CODE_LIST
    for i in range(len(CODE_LIST)): 
        # if match, assign respective morse code to value_up
        if value == CODE_LIST[i][check]:
            valid_value = CODE_LIST[i][output]
    
    return valid_value

def alpha_to_morse():
    '''
        Test Case #1
            Hello, world!
            .... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--
        Test Case #2
            Andiamo a cena
            .- -. -.. .. .- -- --- / .- / -.-. . -. .-
        Test Case #3
            email@address.com
            One of the characters you entered is invalid. 
            Please choose a different phrase
    '''
    # welcome message
    print('Enter your alphanumeric message and I will convert it into a' +
    ' morse code message. To kill the application user the' +
    ' :q: escape character.')
    
    # run the app unless the user enter :q:
    while True:
        # ask user to enter a phrase
        alpha = input('Enter your phrase: ')
        # convert function parameter into uppercase character
        alpha_up = alpha.upper()
        # if user enters escape character, kill the app
        if alpha == ESCAPE_CHAR:
            break

        morse_list = []
        # variable to check whether or not the user entered a valid phrase
        is_valid = True
        # run check_char for each character in the phrase 
        for j in range(len(alpha_up)):
            alpha_char = alpha_up[j]
            # if character is valid, append it to the morse_list empty list
            if check(alpha_char,CODE_LETTER,CODE_SEQUENCE) != INVALID_CHAR:
                add_morse_char = check(alpha_char,CODE_LETTER,CODE_SEQUENCE)
                morse_list.append(add_morse_char)
            # if the character is NOT valid, change is_valid to false
            else:
                is_valid = False
        # if is_valid equals True, convert list of morse codes into a string
        # and print it 
        if is_valid:
            morse_code = ' '
            morse_final = morse_code.join(morse_list)
            print('Your Morse code: ', morse_final)
        # if is_valid equals False, alert user character is invalid
        else:
            print('One of the characters you entered is invalid.' + 
            ' Please choose a different phrase.')
    print('Start over!')

def morse_to_alpha():
    '''
        Test Case #1
            .. / .- -- / .- / - . ... - -.-.--
            I AM A TEST!
        Test Case #2
            --- .... / ... --- .-.. . / -- .. --- --..-- / .. --- / ... . -. --.. .- / - . -.-.--
            Oh sole mio, io senza te!
        Test Case #3
            .---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----. .---- -----
            123456789910
    '''
    # welcome message
    print('Enter your morse code message and I will convert it into an' +
    ' alphanumeric sentence. Be sure to add a space between each Morse Code' +
    ' character and a / between words. To kill the application user the' +
    ' :q: escape character.')

    while True:
        morse_code = input('Enter a your Morse Code: ')

        if morse_code != ESCAPE_CHAR:
            code_list = morse_code.split()

            alpha_sentence = []
            for j in range(len(code_list)):
                morse = code_list[j]
                # if character is valid, append it to the morse_list empty list
                if check(morse, CODE_SEQUENCE, CODE_LETTER) != INVALID_CHAR:
                    add_alpha_char = check(morse, CODE_SEQUENCE, CODE_LETTER)
                    alpha_sentence.append(add_alpha_char)
            
            alpha_sentence_string = ''
            alpha_sentence_final = alpha_sentence_string.join(alpha_sentence)
            print('Your alphanumeric phrase: ', alpha_sentence_final)
        if morse_code == ESCAPE_CHAR:
            break
    print('Start over!')

def main():
    '''
        Hello
    '''
    print('Welcome Morse Code Application!')
    
    while True:
        choice = input('Choose one of the options below to start.\n' + 
            OPTION_A + '. Convert from Alpha to Morse Code\n'
            + OPTION_B + '. Convert from Morse Code to Alpha\n'
            + OPTION_C + '. Quit the the app\n')

        choice_formatted = choice.upper()

        if choice_formatted == OPTION_A:
            alpha_to_morse()
        elif choice_formatted == OPTION_B:
            morse_to_alpha()
        elif choice_formatted == OPTION_C:
            break
        else:
            print('Sorry, you entered an invalid option. Please choose' +
            ' from one of the options below.')
    print('Thank you for using the app. Bye!')
main()


