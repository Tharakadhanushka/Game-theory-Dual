import numpy as np
import random

def cal_possibility():
    num_instances = 0
    for dice1 in range(1,7):
        for dice2 in range(1,7):
            for dice3 in range(1,7):
                for dice4 in range(1,7):
                    for dice5 in range(1,7):
                        for dice6 in range(1,7):
                            for dice7 in range(1,7):
                                for dice8 in range(1,7):
                                    for dice9 in range(1,7):
                                        for dice10 in range(1,7):
                                            #Cheking total
                                            if(dice1 + dice2 + dice3 + dice4
                                                +dice5 + dice6 + dice7 + dice8 + dice9+ dice10) == 32:
                                                num_instances += 1

    print("\t Number of Instances(Total = 32 ): {}".format(num_instances))
    return num_instances

if __name__ == "__main__":
    total_of_possibilities = cal_possibility()
    total_num_of_instances = 6 ** 10
    print("\t Total number of instances : {}".format(total_num_of_instances))
    print("\t Probability: {}".format(total_of_possibilities/total_num_of_instances))               

