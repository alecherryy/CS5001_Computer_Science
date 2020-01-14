''' 
    Alessia Pizzoccheri - CS 5001 02

    Consulted https://www.programiz.com/python-programming/methods/list/index 
    to check how to print an item's index. I couldn't remember.
'''

from mbta import is_valid_station
from mbta import get_direction
from mbta import get_num_stops


def test_invalid_station():
    '''
        Function test_invalid_station
        Input: Nothing
        Returns: int
        Does: Invokes the is_valid_station function on several different
        inputs, expecting the function to return False. Counts the
        number of times it returns True instead, recording them
        as fails.
    '''
    num_failed = 0

    # Test Case 1: cesena, False, SUCCESS
    test_station = 'cesena'

    print('STATION INPUT TEST --',test_station)
    if is_valid_station(test_station) == False:
        print('This stop is not on the Red Line. SUCCESS!\n')
    else:
        print('This stop is on the Red Line. FAIL!\n')
        num_failed += 1

    # Test Case 2: MILAN, False, SUCCESS
    test_station = 'MILAN'

    print('STATION INPUT TEST --',test_station)
    if is_valid_station(test_station) == False:
        print('This stop is not on the Red Line. SUCCESS!\n')
    else:
        print('This stop is on the Red Line. FAIL!\n')
        num_failed += 1
    
    # Test Case 3: JFK-UMass, False, SUCCESS
    test_station = 'JFK-UMass'

    print('STATION INPUT TEST --',test_station)
    if is_valid_station(test_station) == False:
        print('This stop is not on the Red Line. SUCCESS!\n')
    else:
        print('This stop is on the Red Line. FAIL!\n')
        num_failed += 1
    
    # Test Case 4: South Station, False, SUCCESS
    test_station = 'SouthStation'

    print('STATION INPUT TEST --',test_station)
    if is_valid_station(test_station) == False:
        print('This stop is not on the Red Line. SUCCESS!\n')
    else:
        print('This stop is on the Red Line. FAIL!\n')
        num_failed += 1

    return num_failed

def test_valid_station():
    '''
        Function test_valid_station
        Input: Nothing
        Returns: int
        Does: Invokes the is_valid_station function on several different
        inputs, expecting the function to return True. Counts the
        number of times it returns False instead, recording them
        as fails.
    '''
    num_failed = 0

    # Test Case 1: pOrter, True, SUCCESS
    test_station = 'Porter'
    
    print('STATION INPUT TEST --',test_station)
    if is_valid_station(test_station):
        print('This stop is on the Red Line. SUCCESS!\n')
    else:
        print('This stop is not on the Red Line. FAIL!\n')
        num_failed += 1
    
    # Test Case 2: ASHMONT, True, SUCCESS
    test_station = 'ASHMONT'

    print('STATION INPUT TEST --',test_station)
    if is_valid_station(test_station):
        print('This stop is on the Red Line. SUCCESS!\n')
    else:
        print('This stop is not on the Red Line. FAIL!\n')
        num_failed += 1
    
    # Test Case 3: downtown crossing, True , SUCCESS
    test_station = 'Downtown Crossing'

    print('STATION INPUT TEST --',test_station)
    if is_valid_station(test_station):
        print('This stop is on the Red Line. SUCCESS!\n')
    else:
        print('This stop is not on the Red Line. FAIL!\n')
        num_failed += 1
    
    # Test Case 3: charles/mgh, True , SUCCESS
    test_station = 'charles/mgh'

    print('STATION INPUT TEST --',test_station)
    if is_valid_station(test_station):
        print('This stop is on the Red Line. SUCCESS!\n')
    else:
        print('This stop is not on the Red Line. FAIL!\n')
        num_failed += 1

    return num_failed

def test_get_valid_direction():
    '''
        Function test_get_direction
        Input: Nothing
        Returns: int
        Does: Invokes the get_direction function on several different
        inputs, expecting the function to return None
    '''
    num_failed = 0

    # Test Case 1: Ashmont, Ruggles, returns String, SUCCESS
    test_start_station = 'Ashmont'
    test_end_station = 'Ruggles'

    print('STATION INPUT TEST --',test_start_station,'and',test_end_station)
    if get_direction(test_start_station,test_end_station):
        print(get_direction(test_start_station,test_end_station))
        print('This stop is on the Red Line. SUCCESS!\n')
    else:
        print('This stop is not on the Red Line. FAIL!\n')
        num_failed += 1
    
    # Test Case 2: PARK ST, ceNTral, returns String, SUCCESS
    test_start_station = 'PARK ST'
    test_end_station = 'ceNTRal'

    print('STATION INPUT TEST --',test_start_station,'and',test_end_station)
    if get_direction(test_start_station,test_end_station):
        print('This stop is on the Red Line. SUCCESS!\n')
    else:
        print('This stop is not on the Red Line. FAIL!\n')
        num_failed += 1
    
    # Test Case 3: PorteR, ALEWIfe, returns String, SUCCESS
    test_start_station = 'ALEWIfe'
    test_end_station = 'PorteR'

    print('STATION INPUT TEST --',test_start_station,'and',test_end_station)
    if get_direction(test_start_station,test_end_station):
        print('This stop is on the Red Line. SUCCESS!\n')
    else:
        print('This stop is not on the Red Line. FAIL!\n')
        num_failed += 1
    
    # Test Case 4: Downtown CROSSING, ALEWIfe, returns String, SUCCESS
    test_start_station = 'Downtown CROSSING'
    test_end_station = 'Savin Hill'

    print('STATION INPUT TEST --',test_start_station,'and',test_end_station)
    if get_direction(test_start_station,test_end_station):
        print('This stop is on the Red Line. SUCCESS!\n')
    else:
        print('This stop is not on the Red Line. FAIL!\n')
        num_failed += 1

    return num_failed

def test_get_invalid_direction():
    '''
        Function test_get_invalid_direction
        Input: Nothing
        Returns: int
        Does: Invokes the get_direction function on several different
        inputs, expecting the function to return 'Destination not found'.
    '''
    num_failed = 0

    # Test Case 1: cesena, Ruggles, returns String, SUCCESS
    test_start_station = 'cesena'
    test_end_station = 'Ruggles'

    print('STATION INPUT TEST --',test_start_station,'and',test_end_station)
    if get_direction(test_start_station,test_end_station):
        print('Not a valid stop on the Red Line. SUCCESS!\n')
    else:
        print('A valid stop on the Red Line. FAIL!\n')
        num_failed += 1
    
    # Test Case 2: Alewife, Alewife, returns String, SUCCESS
    test_start_station = 'Alewife'
    test_end_station = 'Alewife'

    print('STATION INPUT TEST --',test_start_station,'and',test_end_station)
    if get_direction(test_start_station,test_end_station):
        print('Not a valid stop on the Red Line. SUCCESS!\n')
    else:
        print('A valid stop on the Red Line. FAIL!\n')
        num_failed += 1
    
    # Test Case 3: savinHill, , returns String, SUCCESS
    test_start_station = 'savinHill'
    test_end_station = ''

    print('STATION INPUT TEST --',test_start_station,'and',test_end_station)
    if get_direction(test_start_station,test_end_station):
        print('Not a valid stop on the Red Line. SUCCESS!\n')
    else:
        print('A valid stop on the Red Line. FAIL!\n')
        num_failed += 1
    
    # Test Case 3: , , returns String, SUCCESS
    test_start_station = ''
    test_end_station = ''

    print('STATION INPUT TEST --',test_start_station,'and',test_end_station)
    if get_direction(test_start_station,test_end_station):
        print('Not a valid stop on the Red Line. SUCCESS!\n')
    else:
        print('A valid stop on the Red Line. FAIL!\n')
        num_failed += 1
    
    # Test Case 4: , , returns String, SUCCESS
    test_start_station = 'Charles MGH'
    test_end_station = 'JFK/UMass'

    print('STATION INPUT TEST --',test_start_station,'and',test_end_station)
    if get_direction(test_start_station,test_end_station):
        print('Not a valid stop on the Red Line. SUCCESS!\n')
    else:
        print('A valid stop on the Red Line. FAIL!\n')
        num_failed += 1

    return num_failed

def test_get_valid_num_stops():
    '''
        Function test_get_valid_num_stops
        Input: Nothing
        Returns: int
        Does: Invokes the get_num_stops function on several different
        inputs, expecting the function to return an int greater than 0.
    '''
    num_failed = 0

    # Test Case 1: savin HILL, Shawmut, 2, SUCCESS
    test_start_station = 'savin HILL'
    test_end_station = 'Shawmut'
    expected_result = 2
    actual_result = get_num_stops(test_start_station,test_end_station)

    print('STATION INPUT TEST --',test_start_station,'and',test_end_station)
    if actual_result == expected_result:
        print('Expected result:',expected_result,'Actual result:',actual_result,'SUCCESS!\n')
    else:
        print('Invalid input. FAIL!\n')
        num_failed += 1
    
    # Test Case 2: Ashmont, Alewife, 16, SUCCESS
    test_start_station = 'Ashmont'
    test_end_station = 'Alewife'
    expected_result = 16
    actual_result = get_num_stops(test_start_station,test_end_station)

    print('STATION INPUT TEST --',test_start_station,'and',test_end_station)
    if actual_result == expected_result:
        print('Expected result:',expected_result,'Actual result:',actual_result,'SUCCESS!\n')
    else:
        print('Invalid input. FAIL!\n')
        num_failed += 1
    
    # Test Case 3: Andrew, Broadway, 1, SUCCESS
    test_start_station = 'Andrew'
    test_end_station = 'Broadway'
    expected_result = 1
    actual_result = get_num_stops(test_start_station,test_end_station)

    print('STATION INPUT TEST --',test_start_station,'and',test_end_station)
    if actual_result == expected_result:
        print('Expected result:',expected_result,'Actual result:',actual_result,'SUCCESS!\n')
    else:
        print('Invalid input. FAIL!\n')
        num_failed += 1
    
    # Test Case 4: Porter, Broadway, 8, SUCCESS
    test_start_station = 'Porter'
    test_end_station = 'Broadway'
    expected_result = 8
    actual_result = get_num_stops(test_start_station,test_end_station)

    print('STATION INPUT TEST --',test_start_station,'and',test_end_station)
    if actual_result == expected_result:
        print('Expected result:',expected_result,'Actual result:',actual_result,'SUCCESS!\n')
    else:
        print('Expected result:',expected_result,'Actual result:',actual_result,'FAIL!\n')
        num_failed += 1

    return num_failed

def test_get_invalid_num_stops():
    '''
        Function test_get_valid_num_stops
        Input: Nothing
        Returns: int
        Does: Invokes the get_num_stops function on several different
        inputs, expecting the function to return an int greater than 0.
    '''
    num_failed = 0

    # Test Case 1: Savin Hill, Savin Hill, 0, SUCCESS
    test_start_station = 'Savin Hill'
    test_end_station = 'Savin Hill'
    expected_result = 0
    actual_result = get_num_stops(test_start_station,test_end_station)

    print('STATION INPUT TEST --',test_start_station,'and',test_end_station)
    if actual_result == expected_result:
        print('Expected result:',expected_result,'Actual result:',actual_result,'SUCCESS!\n')
    else:
        print('Invalid input. FAIL!\n')
        num_failed += 1
    
    # Test Case 2: Cesena, Porter, 0, SUCCESS
    test_start_station = 'Cesena'
    test_end_station = 'Porter'
    expected_result = 0
    actual_result = get_num_stops(test_start_station,test_end_station)

    print('STATION INPUT TEST --',test_start_station,'and',test_end_station)
    if actual_result == expected_result:
        print('Expected result:',expected_result,'Actual result:',actual_result,'SUCCESS!\n')
    else:
        print('Invalid input. FAIL!\n')
        num_failed += 1
    
    # Test Case 3: ALEWIFE, alewife, 0, SUCCESS
    test_start_station = 'ALEWIFE'
    test_end_station = 'alewife'
    expected_result = 0
    actual_result = get_num_stops(test_start_station,test_end_station)

    print('STATION INPUT TEST --',test_start_station,'and',test_end_station)
    if actual_result == expected_result:
        print('Expected result:',expected_result,'Actual result:',actual_result,'SUCCESS!\n')
    else:
        print('Invalid input. FAIL!\n')
        num_failed += 1

    return num_failed

def main():
    
    # testing is_valid_station with invalid name stations
    print('Testing is_valid_station() with invalid names for stations.')
    num_fails = test_invalid_station()
    if num_fails == 0:
        print('All valid tests passed!\n\n')
    else:
        print('Sorry, something failed. Go back and fix pls.\n\n')
    
    # testing is_valid_station with valid name stations
    print('Testing is_valid_station() with valid names for stations.')
    num_fails = test_valid_station()
    if num_fails == 0:
        print('All valid tests passed!\n\n')
    else:
        print('Sorry, something failed. Go back and fix pls.\n\n')
    
    # testing get_direction() with invalid name stations
    print('Testing get_direction() with invalid names for stations.')
    num_fails = test_invalid_station()
    if num_fails == 0:
        print('All valid tests passed!\n\n')
    else:
        print('Sorry, something failed. Go back and fix pls.\n\n')
    
    # testing get_direction() invalid name stations
    print('Testing get_direction() with valid names for stations.')
    num_fails = test_get_invalid_direction()
    if num_fails == 0:
        print('All valid tests passed!\n\n')
    else:
        print('Sorry, something failed. Go back and fix pls.\n\n')
    
    # testing get_num_stops() with valid name stations
    print('Testing get_num_stops() with valid names for stations.')
    num_fails = test_get_valid_num_stops()
    if num_fails == 0:
        print('All valid tests passed!\n\n')
    else:
        print('Sorry, something failed. Go back and fix pls.\n\n')
    
    # testing get_num_stops() with invalid name stations
    print('Testing get_num_stops() with invalid names for stations.')
    num_fails = test_get_invalid_num_stops()
    if num_fails == 0:
        print('All valid tests passed!\n\n')
    else:
        print('Sorry, something failed. Go back and fix pls.\n\n')
    
main()