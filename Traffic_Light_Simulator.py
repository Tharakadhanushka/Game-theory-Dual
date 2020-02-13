import numpy as np
from random import seed
from random import random
import matplotlib.pyplot as plt

def go(green_cycles,cars,cars_out,light,green_timer):
    
    if (green_timer<green_cycles*10):
        light='g'
        if (cars>=8):    
            cars_out=8
        else:
            cars_out=cars   
        cars=cars-cars_out;
        green_timer=green_timer + 10

    elif (green_timer==green_cycles*10):   
        if (cars>=8):
            cars_out=8;
        else:
            cars_out=cars    
        cars=cars-cars_out
        light='r'
        green_timer=0
        
    return(cars, cars_out, light, green_timer)

def stop(red_cycles,cars,cars_out,light,red_timer):
    if (red_timer<red_cycles*10):
        light='r'
        cars_out=0;
        red_timer=red_timer + 10

    elif(red_timer==red_cycles*10):
        light='g'
        cars_out=0
        red_timer=0

    return(cars, cars_out, light,red_timer)


cars=0
cars_in=0
cars_out=0
temp_cars_out=0
car_wait_cycle=0
p=0.3
light='r'
green_cycles=6;
red_cycles=2;
green_timer=0
red_timer=0

ncycles=40
#seed(3)
car_waiting =np.zeros(ncycles)  # An array with 40 zeros
cars_in_per_cycle =np.zeros(ncycles)
for i in range(0,ncycles):
    cars_new=0;
    for j in range(0, 10):  # Checking the posibility of 10 vehilces arriving at the light for 10 second block
        if (random()< p):  #p is the threshold
            cars_new=cars_new+1
    #cars_new=sum(r<p);   Matlab Syntax
    cars=cars+cars_new;
    cars_in=cars_in+cars
    cars_in_per_cycle[i]=cars_new

    if (light=='g'):
        (cars, cars_out, light, green_timer)=go(green_cycles,cars,cars_out,light,green_timer)
    else:
        (cars, cars_out, light, red_timer)=stop(red_cycles,cars,cars_out,light,red_timer) 
    cars_out=cars_out+temp_cars_out;
    temp_cars_out=cars_out;
    car_wait_cycle=car_wait_cycle+cars;
    car_waiting[i]=cars;    # This is a column vector

print("No of cycles = " ,i+1)
Total_time=10*i+1;
print("Simulated Time = ",Total_time)
print("No of cars in = ",cars_in)
print("No of cars out = ",cars_out)
print("No of cars waiting = ",car_wait_cycle)
print("Percentage Out/In = ",round(cars_out/cars_in*100),'%')


    
cycles=np.array(range(1,ncycles+1))   # 1, 2, ..... upto 40. 
#cycles=range(1,41,1)
plt.subplot(121)  #(2 colums, 1raw)
plt.plot(cycles, car_waiting, '-', color='blue')
plt.xlabel('Cycle Number')
plt.ylabel('Number of Cars')
plt.gca().set_title('Number of Cars Waiting at the Light')

plt.subplot(122)
plt.bar(cycles, cars_in_per_cycle) 
#plt.plot(cycles, cars_in_per_cycle, '.', color='red')
plt.xlabel('Cycle Number')
plt.ylabel('Number of Cars in')
plt.gca().set_title('Number of Cars in')


plt.show()
