''' 
    Alessia Pizzoccheri - CS 5001 02

'''
import random
import turtle
import kmeans_viz

DATA = [ 
    [-32.97, -21.06], [9.01, -31.63], [-20.35, 28.73], [-0.18, 26.73],
    [-25.05, -9.56], [-0.13, 23.83], [19.88, -18.32], [17.49, -14.09],
    [17.85, 27.17], [-30.94, -8.85], [4.81, 42.22], [-4.59, 11.18],
    [9.96, -35.64], [24.72, -11.39], [14.44, -43.31], [-10.49, 33.55],
    [4.24, 31.54], [-27.12, -17.34], [25.24, -12.61], [20.26, -4.7],
    [-16.4, -19.22], [-15.31, -7.65], [-26.61, -20.31], [15.22, -30.33],
    [-29.3, -12.42], [-50.24, -21.18], [-32.67, -13.11], [-30.47, -17.6],
    [-23.25, -6.72], [23.08, -9.34], [-25.44, -6.09], [-37.91, -4.55],
    [0.14, 34.76], [7.93, 49.21], [-6.76, 12.14], [-19.13, -2.24],
    [12.65, -7.23], [11.25, 25.98], [-9.03, 22.77], [9.29, -26.2],
    [15.83, -1.45], [-22.98, -27.37], [-25.12, -23.35], [21.12, -26.68],
    [20.39, -24.66], [26.69, -28.45], [-45.42, -25.22], [-8.37, -21.09],
    [11.52, -16.15], [7.43, -32.89], [-31.94, -11.86], [14.48, -10.08],
    [0.63, -20.52], [9.86, 13.79], [-28.87, -17.15], [-29.67, -22.44],
    [-20.94, -22.59], [11.85, -9.23], [30.86, -21.06], [-3.8, 22.54],
    [-5.84, 21.71], [-7.01, 23.65], [22.5, -11.17], [-25.71, -14.13],
    [-32.62, -15.93], [-7.27, 12.77], [26.57, -13.77], [9.94, 26.95],
    [-22.45, -23.18], [-34.7, -5.62], [29.53, -22.88], [0.7, 31.02],
    [-22.52, -10.02], [-23.36, -14.54], [-19.44, -12.94], [-0.5, 23.36],
    [-45.27, -19.8], [8.95, 13.63], [47.16, -14.46], [5.57, 4.85],
    [-19.03, -25.41], [28.16, -13.86], [-15.42, -14.68], [10.19, -25.08],
    [0.44, 23.65], [-20.71, -20.94], [35.91, -20.07], [42.81, -21.88],
    [5.1, 9.33], [-15.8, -18.47], [5.39, -26.82], [-40.53, -17.16],
    [-29.54, 23.72], [7.8, 23.4], [-22.19, -27.76], [-23.48, -25.01],
    [-21.2, -21.74], [23.14, -24.14], [-28.13, -13.04], [-24.38, -6.79] ]

SQUARE_ROOT = 0.5
POWER = 2
NUM_CENTROIDS = 4
DISTANCE = 100000000
COLORS = ['Purple','Red','Blue','Orange']

def initialize_centroids():
    '''
        Name: initialize_centroids
        Parameters: None
        Return: list
    '''
    centroids = []

    # pick 4 random centroids from DATA
    while len(centroids) < NUM_CENTROIDS:
        point = random.choice(DATA)

        # if centroid does not match existing centroids
        # append to the list
        if point not in centroids:
            centroids.append(point)

    return centroids

def euclidean(a,b):
    '''
        Name: euclidean
        Parameters: list,list
        Return: float
    '''
    # calculate Euclidean distance
    x = ( a[0] - b[0] ) ** POWER
    y = ( a[1] - b[1] ) ** POWER
    tot = ( x + y )
    distance = tot ** SQUARE_ROOT

    return distance

def create_cluster(centroids):
    '''
        Name: create_cluster
        Parameter: nested list
        Return: nested list
    '''
    assignment = []

    for i in range(len(DATA)):
        min_distance = DISTANCE
        centroid_index = None

        for p in range(len(centroids)):
            # calculate Euclidean distance for each DATA and centroids
            distance = euclidean(DATA[i],centroids[p])

            # if new distance less than the current one, update new distance
            if distance < min_distance:
                min_distance = distance
                centroid_index = p
        
        # create assignment pair and append it to assignment list
        assignment_pairs = [i,centroid_index]
        assignment.append(assignment_pairs)

    return assignment

def optimize_centroids(centroids,assignment):
    '''
        Name; optimize_centroids
        Parameter: nested list, nested list
        Return: nested list
    '''
    new_centroids = []

    for i in range(len(centroids)):
        # empty lists for the x and coordinates
        x_coordinates = []
        y_coordinates = []

        # assign each DATA pair value to respective centroid
        for j in range(len(assignment)):
            if assignment[j][1] == i:
                data_index = assignment[j][0]
                x_coordinates.append(DATA[data_index][0])
                y_coordinates.append(DATA[data_index][1])
        
        # sum total values of x and total values of y
        x_tot = sum(x_coordinates)
        y_tot = sum(y_coordinates)
        
        # calculate the average value of x coordinate and y coordinate
        x_average = x_tot / len(x_coordinates)
        y_average = y_tot / len(y_coordinates)

        # assign new coordinates to each centroid
        pair = [x_average,y_average]

        # append pairs to empty new centroids list
        new_centroids.append(pair)

    return new_centroids


def main():

    # create centroids
    centroids = initialize_centroids()
    
    # create assignment list of centroids and DATA
    assignment = create_cluster(centroids)

    # uncomment line 141 and 142 to see initial centroids
    # kmeans_viz.draw_centroids(centroids,COLORS)
    # kmeans_viz.draw_assignment(centroids, DATA, assignment, COLORS)

    # improve centroids' coordinates
    centroids = optimize_centroids(centroids,assignment)
    
    # update assignment based on improved centroids
    assignment = create_cluster(centroids)
    
    # draw clusters
    kmeans_viz.draw_centroids(centroids,COLORS)
    kmeans_viz.draw_assignment(centroids, DATA, assignment, COLORS)

main()