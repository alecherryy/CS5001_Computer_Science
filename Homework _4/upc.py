''' 
    Alessia Pizzoccheri - CS 5001 02
'''

MODULUS = 10
MULTIPLY = 3
ZERO = 0
MIN = 2

# I created a separate function to check for zeroes before the
# main program starts running
def check_zeroes(lst):
    ''' 
        Function check_zeroes
        Input: lst
        Returns: bool
    '''
    tot = 0

    # iterate through list and sum together the value of 
    # each item
    for num in lst:
        tot += num
    
    # if the total is zero return True
    if tot == ZERO:
        return True
    else:
        return False

def is_valid_upc(upc_code):
    ''' 
        Function is_valid_upc
        Input: lst
        Returns: bool

        Test Case #1:
        0 7 3 8 5 4 0 0 8 0 8 9
        True
        
        Test Case #2:
        0 0 0 0 0
        False
        
        Test Case #3:
        9
        False
        
        Test Case #4:
        0 8 2 8 4 5 9 0 7 0 9 1
        False
        
        Test Case #5:
        1 9 4 0 9 5 5 8 3 3 0 9
        True
    '''

    total = 0
    even = 0
    odd = 0
    zeroes = check_zeroes(upc_code)
    is_valid = True

    # if the upc code is less than 2 numbers or check_zeroes returns True
    if len(upc_code) < MIN or zeroes:
        is_valid = False
    else:
        # sum numbers at even position
        for i in range(len(upc_code)-1,0-1,-2):
            even += upc_code[i]
        
        # sum numbers at odd position and multiply by 3
        for i in range(len(upc_code)-2,0-1,-2):
            odd += upc_code[i] * MULTIPLY
        
        # sum everything together
        total = (odd + even)

    # final check to see if the UPC code is a multiple of 10
    if total % MODULUS == ZERO:
        is_valid = True
    else:
        is_valid = False
    
    return is_valid