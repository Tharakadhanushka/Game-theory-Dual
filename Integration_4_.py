# Finding the area under y = 0.5x+0.5 line and y= x^2 curve between the limits [a,b]

import numpy as np
from random import random

def curve(xval):
    yval = xval**2
    return yval

def curve2(xval):
    yval = -(xval)**2+8
    return yval


def Area(a,b,function):
    def func(xval):
        yval = function(xval)
        return yval
       
    def max_yval(a,b):
        temp_x = np.arange(a,b+0.1,0.1)   #(start value,end,increment) end is not included.need to have a vlue just above b
        temp_y = func(temp_x)          #temp_x**2      # y = f(x) = x**2
        max_y =  temp_y.max()
        return max_y
    
    max_Px = max_yval(a,b) 
    N = 0
    M = 0
    num =100000
    for i in range(0,num):
        x =  a + (b-a)*random()  #x value between [a,b]
        y =  0 + (max_Px-0)*random()  #y value between [0,max_Px]
        yval = func(x)
        if( y <= yval ):
            M = M + 1       
        N = N + 1


    Area = max_Px*(b-a)*M/N
    print("Area = ", Area)
    return Area

a = -2   # lower limit
b = 2      # upper limit
Area_under_curve = Area(a,b,curve)
Area_under_line  = Area(a,b,curve2)

Area_shaded = Area_under_line - Area_under_curve
print("Area Shaded = ",Area_shaded)


