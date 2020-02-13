import numpy as np

def get_function(x_val):
    return (1/x_val)

if __name__ =="__main__":
    N=4
    start_val=1
    end_val=2
    h_val=(end_val-start_val)/2

    area = (h_val/3) * (get_function(start_val) + 4 * get_function((start_val+end_val)/2)+ get_function(end_val) )
    print("area  :",str(area))
