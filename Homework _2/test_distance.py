'''
    Alessia Pizzoccheri - CS 5001 02

    This script is meant to test absolute() and manhattan() from distance.py

    While hand writing the test cases for manhattan() I realized I was converting the arguments to 
    their absolute value first. My function was correct tho.

    As I finished writing the script, I decided to add 3 branches to my if statement in main(). 
    If my test functions fail, I want to know which function failed and how many times at first glance.
'''

from distance import absolute
from distance import manhattan

# using EPSILON to test accuracy between expected and actual results
EPSILON = .0001

# test absolute() function from absolute.py
def test_absolute():
    ''' Function: test_absolute
        Input: none
        Returns: int, # of tests that failed
        Does: tests a few different inputs on the euclidean
            distance function, makes sure each distance value
            is as-expected.
    '''
    num_failed = 0
    
    # Test 1: (0)
    # Absolute value should be 0
    actual = absolute(0)
    expected = 0.0
    print('Input (0).\n'
        'Expected result', expected,
        'and actual result =', actual)
    if actual == expected and actual >= 0:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    # Test 2: (5.253)
    # Absolute value should be 5.253
    actual = absolute(5.253)
    expected = 5.253
    print('Input (0).\n'
        'Expected result', expected,
        'and actual result =', actual)
    if actual == expected and actual >= 0:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    # Test 3: (-0.0023)
    # Absolute value should be 0.0023
    actual = absolute(-0.0023)
    expected = 0.0023
    print('Input (0).\n'
        'Expected result', expected,
        'and actual result =', actual)
    if actual == expected and actual >= 0:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    # Test 4: (-12)
    # Absolute value should be 12
    actual = absolute(-12)
    expected = 12
    print('Input (0).\n'
        'Expected result', expected,
        'and actual result =', actual)
    if actual == expected and actual >= 0:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1

    return num_failed

def test_manhattan():
    ''' Function: test_manhattan
        Input: none
        Returns: int, # of tests that failed
        Does: tests a few different inputs on the manhattan
            distance function, makes sure each distance value
            is as-expected.
    '''

    num_failed = 0
    
    # Test 1: (0)
    # Absolute value should be 0
    actual = manhattan(0,0,0,0)
    expected = 0.0
    print('Input (0).\n'
        'Expected result', expected,
        'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    # Test 2: (-1.235, 0, 2.47, 5.732)
    # Absolute value should be 0
    actual = manhattan(-1.235, 0, 2.47, 5.732)
    expected = 9.4370
    print('Input (0).\n'
        'Expected result', expected,
        'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    # Test 3: (137.88, 48.01, 93.12, 47.99)
    # Absolute value should be 0
    actual = manhattan(137.88, 48.01, 93.12, 47.99)
    expected = 44.7799
    print('Input (0).\n'
        'Expected result', expected,
        'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    # Test 4: (3.18, 15, 27.891, 4)
    # Absolute value should be 0
    actual = manhattan(3.18, 15, 27.891, 4)
    expected = 35.711
    print('Input (0).\n'
        'Expected result', expected,
        'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1

    return num_failed

def main():
    abs_fail = test_absolute()
    man_fail = test_manhattan()
    
    # if fails, the if statement below lets you know which function failed so you can narrow your search. 
    # If both fail, it will output the number of fails for each function
    if abs_fail == 0 and man_fail == 0:
        print('ALL TESTS PASSED!')
    elif abs_fail == 0 and man_fail != 0:
        print('Sorry manhattan() failed', man_fail, 'time(s). Please go back and fix.')
    elif man_fail == 0 and abs_fail != 0:
        print('Sorry, abolute() failed', abs_fail, 'time(s). Please go back and fix.')
    elif man_fail != 0 and abs_fail != 0:
        print('Sorry, abolute() failed', abs_fail, 'time(s) and manhattan() failed', man_fail, 
        'time(s). Please go back and fix.')
main()