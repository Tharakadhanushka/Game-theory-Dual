import numpy as np

def get_y_values(x_val):
    return (1/x_val)

if __name__ =="__main__":
    N=4
    start_val=1
    end_val=2
    h_val=(end_val-start_val)/N

    x_val=np.arange(start_val,end_val+0.1,h_val)
    print (x_val)
    y_list =[]
    for n in x_val:
        y_list.append(get_y_values(n))

    y_values = np.array(y_list)

    area = (1/2)* h_val*((2*y_values).sum() - (y_values[0]+y_values[-1]))
    print("area  :",str(area))
