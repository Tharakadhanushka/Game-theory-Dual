# Finding the area under y = f(x) = 3x/5 + 2 between the limits [a,b]

import numpy as np
from random import random
import matplotlib.pyplot as plt

def func(xval):
    yval = xval**2
    return yval
    

def max_yval(a,b):
    temp_x = np.arange(a,b,0.1)
    temp_y = func(temp_x)          #(3/5)*temp_x +2      # y = f(x) = 3x/5 + 2
    max_y =  temp_y.max()
    return max_y


a = -1
b = 1
max_Px = max_yval(a,b) 


N = 0
M = 0
num =100000
x_array = np.zeros(num)
y_array = np.zeros(num)

x_in = []
y_in = []

for i in range(0,num):
    x =  a + (b-a)*random()  #x value between [a,b]
    y =  0 + (max_Px-0)*random()  #y value between [0,max_Px]
    yval = func(x)
    if( y <= yval ):
        M = M + 1
        x_in.append(x)
        y_in.append(y)
        
    N = N + 1
    x_array[i] = x
    y_array[i] = y

Area = max_Px*(b-a)*M/N
print("Area = ", Area)    
plt.plot(x_array, y_array, '.', color='blue')
plt.plot(x_in, y_in, '.', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_title('y vs x')
plt.show()

