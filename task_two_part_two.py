import numpy as np  
import random

def turn_random(turns):
    return (random.random(), turns+1)

def duel(prob_arr):
    turns = 0
    survivor = None
    players_ref = {'A':0, 'B':1, 'C':2}
    players = [ x for x in players_ref.keys() ]

    while len(players) > 1:
        for player in players:
            randValue,turns = turn_random(turns)
            opponent_player = players[:]
            opponent_player.remove(player)
            
            print("turns",turns)

            print("players",players)
            if player == 'C' and len(opponent_player) == 2: # turns -=1;
                pass 
            else:   
                if randValue <= prob_arr[players_ref[player]]:
                    print("rand_val",randValue)
                    print("shooted_player",player)
                    print("shooted_player_ref",players_ref[player])
                    players.remove(opponent_player[0])
                    print('removed',opponent_player[0])
                
        if len(players) == 1:
            survivor = players_ref[player[0]]
            print("survivor",survivor)
            break
    return (survivor, turns)

if __name__ == "__main__":
    
    times_of_simulations = 1000
    prob_arr = np.array([ 5/6, 4/6, 2/6 ])
    record_of_survior = np.zeros(3)
    number_of_turns = 0

    print("Number of Simulations : {0}".format(times_of_simulations))

    for simulation in range(times_of_simulations):
        survivor,turns = duel(prob_arr)
        record_of_survior[survivor] += 1
        number_of_turns += turns
    print(record_of_survior)
    surviving_probability = np.divide(record_of_survior, times_of_simulations)
    print("\n Surviving probability of \n\n\t A : {0}\n\n\t B : {1}\n\n\t C : {2}".format(surviving_probability[0], surviving_probability[1], surviving_probability[2]))
    average_turns = (number_of_turns/times_of_simulations)
    
    print("\n Average of Turns taken : {0}".format(average_turns))