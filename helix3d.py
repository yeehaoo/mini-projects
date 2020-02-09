"""
Helix Graph Plotter 3D
09/02/2020
github.com/yeehaoo/

This was supposed to be drawn with a graphics library but here it is in graphical form.
Task: to create a function helix(n), where n is the number of points to be plotted, to form equidistant points on a circle.
Now in 3D!
Best run with n > 10 (increases visibility)
"""


#from runes import *
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#overall there are two problems to solve.
#1. x and y coordinates of each rune
#2. z coordinate of each rune to form the helix

#in this solution, quadrants are as follows:
#32
#41

#important methods to solve our problems:
#show(translate(0.25, -0.25, scale(0.1, circle_bb)))
#show(overlay_frac(1/4, corner_bb, heart_bb))

def get_posx(radius, calc_angle, x_multiplier):
    #convert to radians first, store as 5dp float
    calc_angle = calc_angle * 0.01745329
    posx = radius * math.cos(calc_angle) * x_multiplier
    posx = float('%.5f' %(posx))
    return posx

def get_posy(radius, calc_angle, y_multiplier):
    #convert to radians first, store as 5dp
    calc_angle = calc_angle * 0.01745329
    posy = radius * math.sin(calc_angle) * y_multiplier 
    posy = float('%.5f' %(posy))
    return posy

def range_float(end):
    float_list = []
    for i in range(end):
        float_list.append(i*0.5)
        
    return(float_list)

def helix(n):
    if n >= 5:
        size = 2/n #apply with scale()
        radius = 1/2 - 1/n
        angle_increment = 360/n #incremented to curr_angle
        curr_angle = 0 #to keep track of where the current rune is
        posx_list = []
        posy_list = []
        
        for i in range(n):
            #calc_angle refers to angle between posx and y=0 line
            #here we are getting the calculation angle, then passing it to the getters which will perform the calculation as well as determine polarity
            
            x_multiplier = 1
            y_multiplier = 1
            #to determine polarity.
            #x is positive when the rune is on the right side of x=0 line, and negative when the rune is on the left
            #y is positive when the rune is above the y=0 line, and negative when the rune is below the y=0 line
            
            if curr_angle < 90:
                #quadrant 1
                calc_angle = 90 - curr_angle
                y_multiplier = -1
                
            elif curr_angle < 180:
                #quadrant 2
                calc_angle = curr_angle - 90
                
            elif curr_angle < 270:
                #quadrant 3
                calc_angle = 270 - curr_angle
                x_multiplier = -1
            else:
                #quadrant 4
                calc_angle = curr_angle - 270
                x_multiplier = -1
                y_multiplier = -1
                
            posx = get_posx(radius, calc_angle, x_multiplier)
            posy = get_posy(radius, calc_angle, y_multiplier)
            
            posx_list.append(posx)
            posy_list.append(posy)
            print(str(posx) + " " + str(posy))
            
            #problem 1 solved
            #now think of a way to stack the runes
            #problem: the overlay method is written so you can execute once to display everything at once, not stack layer by layer
            #have to figure out a way to consolidate coordinates of runes then display at one shot
            
            curr_angle += angle_increment
                
        
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        #ax.plot3D(posx_list, posy_list, range(n), 'gray')
        posz_list = range_float(n)
        ax.scatter3D(posx_list, posy_list, posz_list, c=posz_list, cmap='Oranges');
        #plt.plot(posx_list, posy_list, 'o')
        plt.show()
