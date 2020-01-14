''' 
    Alessia Pizzoccheri - CS 5001 02

    Consulted https://www.programiz.com/python-programming/methods/list/index 
    to check how to print an item's index. I couldn't remember.

'''

RED_LINE = [
    'Ashmont',
    'Shawmut',
    'Fields Corner',
    'Savin Hill',
    'JFK/UMass',
    'Andrew',
    'Broadway',
    'South Station',
    'Downtown Crossing',
    'Park St',
    'Charles/MGH',
    'Kendall',
    'Central',
    'Harvard',
    'Porter',
    'Davis',
    'Alewife'
    ]

# function to convert station names to lowercase
def format_station_name():
    ''' Function: format_station_name
        Parameter: none
        Returns: lst
    '''
    STATIONS = []

    # convert every station name to lower case
    for i in range(len(RED_LINE)):
        station_names = RED_LINE[i].lower()
        STATIONS.append(station_names)

    return STATIONS

# new constant used by is_valid_station(), get_direction() and get_num_stops()
STATIONS = format_station_name()

def is_valid_station(station_name):
    ''' Function is_valid_station
        Parameter: str
        Returns: bool
    '''
    is_valid = True
    
    # format station name
    station_name_formatted = station_name.lower()
    
    if station_name_formatted not in STATIONS:
        is_valid = False
    
    return is_valid

def get_direction(start_station,end_station):
    ''' Function get_direction
        Parameter: str, str
        Returns: str
    '''
    # message returned to the user if the station name is not valid
    message = 'Destination not found.'
    
    # format station names
    start_station_formatted = start_station.lower()
    end_station_formatted = end_station.lower()

    # check start station
    if start_station_formatted in STATIONS:
        return start_station_formatted
    else:
        return message
    
    # check end station
    if end_station_formatted in STATIONS:
        return end_station_formatted
    else:
        return message

    # check if start station and end station are the same
    if start_station_formatted == end_station_formatted:
        return message 
    else:
        return message

def get_num_stops(start_station,end_station):
    ''' Function get_direction
        Parameter: str, str
        Returns: int
    '''
    tot_stops = 0
    
    # format station names
    start_station_formatted = start_station.lower()
    end_station_formatted = end_station.lower()

    # remove index 0
    for i in range(len(RED_LINE)):
        i += 1

    # check stations are not the same
    if start_station_formatted != end_station_formatted:
        
        # check for valid stations
        if start_station_formatted in STATIONS and end_station_formatted in STATIONS:
            # get index of start station
            start_index = STATIONS.index(start_station_formatted)
            
            # get index of end station
            end_index = STATIONS.index(end_station_formatted)

            # total stops num always positive
            tot_stops = abs(start_index - end_index)

    return tot_stops
