import numpy as np 
import random

def gen_dice_throws(): 

    result_of_dices = []
    for x in range(10):
        result_of_dices.append(random.randrange(1,7))
    return np.array(result_of_dices)


if __name__ == "__main__":
    
    times_of_trows = 500
    number_of_instance = 0 
    probability_value = 0

    print( "Times of simulations: ",times_of_trows)
    for simulation in range(times_of_trows):
        results = gen_dice_throws()
        if np.sum(results) == 32:
            number_of_instance += 1
    print("Number of instance sum (equal to 32):",number_of_instance)
    
    if number_of_instance > 0:
         probability_value = (number_of_instance/times_of_trows)

    print("Probability of get sum 32 (10 dices throws): ",probability_value)
    
    