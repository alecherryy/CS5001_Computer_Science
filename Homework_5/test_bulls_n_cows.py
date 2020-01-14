from bulls_n_cows import *

TEST_GUESSES = [[1,2, 3, 4], [5, 2, 3, 4], [7, 6, 5, 4], [0, 9, 8, 5],
                [2, 4, 6, 8], [1, 3, 5, 7], [1, 2, 0, 9]]

TEST_SECRET = [[1,9,8, 7],[2,4,6, 7], [1,2,0, 9],[7,6,5, 4]]


def test_count_bulls_and_cows():
    ''' Function test_count_bulls_and_cows
        Input: None.
        Returns: Number of failing test conditions for cow/bull sequences
        Do: Test various cow/bull sequences to ensure those counters
            are working as expected. Key cases: 0 cows, 0 bulls;
            4 cows, 0 bulls; 4 bulls, 0 cows, 2 cows, 2 bulls
    '''

    fails = 0

    # Test Case 1
    # Secret code: 8, 9, 2, 4
    # Guess: 3, 5, 0, 1
    # Expected output: 0 bulls and 0 cows
    secret_code = [ 8, 9, 2, 4 ]
    guess = [ 3, 5, 0, 1 ]
    result = count_bulls_n_cows(secret_code,guess)
    expected = [0, 0]
    if result['bulls'] == expected[0] and result['cows'] == expected[1]:
        print('Expected result was',expected,' Actual result was',
        [result['bulls'],result['cows']],'SUCCESS!\n')
    else: 
        fails += 1
    
    # Test Case 2
    # Secret code: 0, 7, 3, 2
    # Guess: 3, 0, 2, 7
    # Expected output: 0 bulls and 4 cows
    secret_code = [ 0, 7, 3, 2 ]
    guess = [ 3, 0, 2, 7 ]
    result = count_bulls_n_cows(secret_code,guess)
    expected = [0, 4]
    
    if result['bulls'] == expected[0] and result['cows'] == expected[1]:
        print('Expected result was',expected,' Actual result was',
        [result['bulls'],result['cows']],'SUCCESS!\n')
    else: 
        fails += 1
    
    # Test Case 3
    # Secret code: 1, 9, 5, 4
    # Guess: 1, 9, 5, 4
    # Expected output: 0 bulls and 4 cows
    secret_code = [ 1, 9, 5, 4 ]
    guess = [ 1, 9, 5, 4 ]
    result = count_bulls_n_cows(secret_code,guess)
    expected = [4, 0]
    
    if result['bulls'] == expected[0] and result['cows'] == expected[1]:
        print('Expected result was',expected,' Actual result was',
        [result['bulls'],result['cows']],'SUCCESS!\n')
    else: 
        fails += 1
    
    # Test Case 4
    # Secret code: 6, 4, 2, 0
    # Guess: 0, 2, 4, 6
    # Expected output: 2 bulls and 2 cows
    secret_code = [ 6, 4, 2, 0 ]
    guess = [ 0, 4, 2, 6 ]
    result = count_bulls_n_cows(secret_code,guess)
    expected = [2, 2]
    
    if result['bulls'] == expected[0] and result['cows'] == expected[1]:
        print('Expected result was',expected,' Actual result was',
        [result['bulls'],result['cows']],'SUCCESS!\n')
    else: 
        fails += 1
    
    # Test Case 5
    # Secret code: 3, 0, 1, 5
    # Guess: 0, 2, 8, 9
    # Expected output: 0 bulls and 1 cows
    secret_code = [ 3, 0, 1, 5 ]
    guess = [ 0, 2, 8, 9 ]
    result = count_bulls_n_cows(secret_code,guess)
    expected = [0, 1]
    
    if result['bulls'] == expected[0] and result['cows'] == expected[1]:
        print('Expected result was',expected,' Actual result was',
        [result['bulls'],result['cows']],'SUCCESS!\n')
    else: 
        fails += 1

    return fails
        

def auto_play_game(secret_code, guess_book):
    ''' Function auto_play_game
        Input:  secret_code (list of digits),
                guess_book (dictionary of guess history)
        Returns: True if auto-player a winner; False otherwise
        Do: Automate the playing of Bulls and Cows for regression
        testing. Instead of using interactive input from stdin, this
        function uses test data fed directly to the function to simulate
        an entire "systems test" and complete game flow
        Concept: instead of guess = input(...), now using
        guess = TEST_GUESSES[i]
    '''

    counter = 0
    history = []
    guess_history = []
    player_won = False

    for i in range(len(secret_code)):
        # play until player wins or player exhausted number of tries
        while True:
            result = count_bulls_n_cows(secret_code[i],guess_book[i]['GUESS'])

            if counter != ROUNDS:

                # if player does not guess
                if guess_book[i]['GUESS'] != secret_code[i]:
                    # kepp count of rounds played
                    counter = counter + 1

                    # create list item with previous guess, round cows and
                    # round bulls
                    guess_history = [guess_book[i]['GUESS'],result['cows'],result['bulls']]

                    # append item to history list
                    history.append(guess_history)

                    print('Your guess history:')

                    for i in range(len(history)):

                        # format history print 
                        print('Your guess:',history[i][0],'Cows:',history[i][1],
                            'Bulls: ',history[i][2])

                # if player guesses secret code
                else:
                    player_won = True
                    break
            # player does not guess and player runs out of rounds
            else: 
                print('Sorry. You lost! ' +
                    'The secret code was',secret_code[i])
                break

    return player_won


def test_regression_bull_cow(secret_code):
    ''' Function test_regression_bull_cow
        Input: secret_code: secret to test with (the one we're "cracking").
        Returns: None
        Do: Automatically exercise and test the entire bulls n cows system
        by calling auto_play_game() multiple times with both "winning" and
        "losing" data. Printed output can then be "diff'd" and examined either
        manually or automatically via tool support

        Example: code is our test data, and autoplay instead of interactive
        secret_code = TEST_SECRET[0]
        guess_book = create_guessbook(7)
        result = auto_play_game(secret_code, guess_book)
    '''

    auto_play_game(secret_code)

    
def main():
    print('Beginning test suite. Testing count bulls and cows...\n')
    
    fails = test_count_bulls_and_cows()
    
    if fails > 0:
        print('Something went wrong. Pls go back and fix errors')
    else:
        print('Counting Bulls and Cows Passed ALL Tests')

    print('Beginning Auto Play Regression Tests')
    # some example calls
    test_regression_bull_cow(TEST_SECRET[0])
    test_regression_bull_cow(TEST_SECRET[1])    

main()
