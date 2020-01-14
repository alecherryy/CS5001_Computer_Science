''' 
    Alessia Pizzoccheri - CS 5001 02

    Haversine function parameters
    distance = haversine(latitude1, longitude1, latitude2, longitude2)

    Test Case #1
    Boston

    Test Case #2
    Miami

    Test Case #3
    Seattle, 47.6062, 122.3321
    7118.43 nautical miles
'''

from haversine import haversine

def main():
    # predefined latitude and longitude for Dorian, Boston and Miami
    DORIAN_LATITUDE = 27.1 
    DORIAN_LONGITUDE = -78.4 
    BOSTON_LATITUDE = 42.361145 
    BOSTON_LONGITUDE = -71.057083 
    MIAMI_LATITUDE = 25.761681 
    MIAMI_LONGITUDE = -80.191788

    # Ask users to pick a location
    print('This is a hurricane tracker based upon the Haversine approach.')
    origin = input('Pick one of the choices below to activate the radar\n' + 
            'A. Boston\n' + 
            'B. Miami\n' +
            'C. I want to pick a different city\n' ).upper()
    
    # If users choose Boston, run Boston coordinates through Haversine script and calculate distance
    if origin == 'A':
        nautical_miles = haversine(BOSTON_LATITUDE,BOSTON_LONGITUDE,DORIAN_LATITUDE,DORIAN_LONGITUDE)
        print('On September 3, 2019 Hurrican Dorian was {:.2f}'.format(nautical_miles),' nautical miles from Boston.')
        if nautical_miles < 150:
            print('WARNING! Seek shelter!')
        else:
            print('You are safe.')

    # If users choose Miami, run Miami coordinates through Haversine script and calculate distance
    elif origin == 'B':
        nautical_miles = haversine(MIAMI_LATITUDE,MIAMI_LONGITUDE,DORIAN_LATITUDE,DORIAN_LONGITUDE)
        print('On September 3, 2019 Hurrican Dorian was {:.2f}'.format(nautical_miles),' nautical miles from Miami.')
        if nautical_miles < 150:
            print('WARNING! Seek shelter!')
        else:
            print('You are safe.')
    
    # If users choose a different city, ask users to manually enter coordinates
    elif origin == 'C':
        print('To check a different city, enter name of the city, the latitude and the longituted.')
        city = input('What is the name of the city? ')
        latitude = float(input("What is the city's latitude? "))
        longitude = float(input("What is the city's longitude?" ))

        # Output final results
        nautical_miles = haversine(latitude,longitude,DORIAN_LATITUDE,DORIAN_LONGITUDE)
        print('On September 3, 2019 Hurrican Dorian was {:.2f}'.format(nautical_miles),' nautical miles from ',city)
        if nautical_miles < 150:
            print('WARNING! Seek shelter!')
        else:
            print('You are safe.')

main()
