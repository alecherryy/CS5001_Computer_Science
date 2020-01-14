'''
Alessia Pizzoccheri
Walk for a Cause

Test Case #1:
    2 km, .5 hr, $5
    1.24 miles, 2.49 mph, 24 mins and 8s, earn $6.21

Test Case #2:
    23 km, 18 hr, $2.34
    14.29 miles, 0.79 mph, 75 mins and 34s, earn $33.44

Test Case #3, aka The money Jim donates to Oscar's nephew's walk-a-thon
    29 km, 15 hr, $3
    18.02 miles, 1.20 mph, 49 mins and 56s, earn $54.06

Test Case #4, aka The money Michael donates to Oscar's nephew's walk-a-thon
    29 km, 18.25 hr, $25
    18.02 miles, 0.99 mph, 60 mins and 45s, earn $450.49

Test Case #5
    11.2 km, 5.89 hr, $2.76
    6.96 miles, 1.18 mph, 50 mins and 46s, earn $19.21
'''

def main():

    # defining all variables
    km_walked = float(input('How many km did you walk? '))
    hours_walked = float(input('How many hours was your walk? '))
    money_per_mile = float(input('How much is your sponsor paying per mile? '))

    # convert km to miles
    miles_walked = km_walked * 0.621371

    # miles per hour 
    miles_per_hour = miles_walked / hours_walked

    # pace per mile
    mins_per_mile = (hours_walked * 60) / miles_walked
    secs_per_mile = (mins_per_mile % int(mins_per_mile)) * 60
    
    # calculate the total amount of money
    total_amount = miles_walked * money_per_mile 

    # show km to mile conversion
    print('You walked a total of {:.2f}'.format(miles_walked), ' miles')
    
    # print pace and total money raised
    print('You walked at an average of {:.2f}'.format(miles_per_hour),'mph')
    print('Your pace was',int(mins_per_mile),'minutes and ',int(secs_per_mile),'seconds per mile')
    print('You raised a total of ${:.2f}'.format(total_amount))


main()
