'''
    Alessia Pizzoccheri - CS 5001 02

    Consulted Stack Overflow for getting absolute value without using the built-in function abs(): 
    https://stackoverflow.com/questions/3854310/how-to-convert-a-negative-number-to-positive
    
    Consulted Stack Overflow for getting square root without using the built-in function sqrt():
    https://www.quora.com/How-do-I-write-square-roots-in-Python

'''

def absolute(n):
    # use absolute to obtain numbers without any negative or positive value. 
    # Since I may not use the abs() built-in function, I am using an if statement 
    # to check whether or not n is negative. If it is negative, I  multiply n 
    # by the negative sign and get a positive number.
    if n < 0:
        n = -n
    return n

def manhattan(x1,y1,x2,y2):
    # the formula to calculate distance is |(x2 - x1)| + |(y2 - y1)|. 
    # I declare two variables, a and b, to calculate the difference between coordinates
    a = x2 - x1
    b = y2 - y1
    # to calculate the distance I call the absolute() function 
    # where a and b are the arguments of the function
    distance = absolute(a) + absolute(b)

    return distance

def euclidean(x1,y1,x2,y2):
    # I declare two variables to calculate the difference between coordinates
    a = x2 - x1
    b = y2 - y1
    
    # To calculate the Euclidean distance, To calculate the Euclidean formula below 
    # I implement python's symbolic mathematics. **2 means 'to the power of 2', 
    # and '**0.5' is the square root
    euclidean_distance = ((a**2) + (b**2))**.5

    return euclidean_distance

