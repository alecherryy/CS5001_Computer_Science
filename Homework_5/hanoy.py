'''
    Alessia Pizzoccheri - CS 5001 02

    Consulted https://stackoverflow.com/questions/22025764/python-check-for-integer-input
    to learn how to prevent interpreter from throwing an error message if user
    input is not an integer
'''
import hanoi_viz
MIN = 1
MAX = 8
SOURCE = 'Start'
MIDDLE = 'Transfer'
TARGET = 'End'

def check_input():
    ''' Name: check_input
        parameters: none
        returns: int
    '''
    while True:
        
        # ask users how many disks in the tower
        user_input = input('How many disks does the Tower of Hanoi have? ')
        
        # check if input is integer and prevent error message
        try:
            num_disks = int(user_input)
        except ValueError:
            print('Please, enter a valid input.')
        else:

            # check int is between 1 and 8 inclusive
            if num_disks >= MIN and num_disks <= MAX:
                break
            # go back to top if int is outside valid range
            else:
                print('Please, enter a valid input.')
                
    return num_disks

def move_tower(disks,source,target,middle,towers):
    '''
        Name: move_tower
        Input: int, dict, dict, dict, dict
        Return: None
    ''' 

    # if there's only one disks
    if disks == 1:
        hanoi_viz.move_disk(source,target,towers)
    # if there are multiple disks
    else:
        move_tower(disks-1,source,middle,target,towers)
        hanoi_viz.move_disk(source,target,towers)
        move_tower(disks-1,middle,target,source,towers)
        

def main():

    print('Welcome to the Tower of Hanoi.\n'+
        'To start, enter an integer between 1 and 8.')

    # select number of disks
    num_disks = check_input()

    # draw the towers
    towers = hanoi_viz.initialize_towers(num_disks,SOURCE,TARGET,MIDDLE)

    # start the Tower of Hanoi
    move_tower(num_disks,SOURCE,TARGET,MIDDLE,towers)
main()