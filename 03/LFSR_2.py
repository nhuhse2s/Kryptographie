####
# This program implements a LFSR: x^21 + x^2 + 1
####

import numpy as np

def Init():
    ## Init with 0x1FFFFF = 111111111111111111111
    flops_current_state = np.array([1]*21)
    flops_previous_state = flops_current_state.copy()
    flops_next_state = flops_current_state.copy()
    out_array = []

    for n_bits in range(0, 64):

        for i in range(21-1, -1, -1):
            #print("i: ", i)
            #print("i-1: ", i-1)
            if((i-1) >= 0):
                flops_next_state[i-1] = flops_current_state[i]
            if((i-1) == -1):
                flops_next_state[20] = flops_current_state[0]^flops_current_state[19]
                #flops_next_state[20] = flops_current_state[0]^flops_current_state[2]     ## Das sollte das korrekte Polynom    
        
        out_array.append(flops_current_state[0])
        flops_current_state = flops_next_state.copy()
            
    return out_array, flops_current_state

def Main():
    result, internal = Init()
    print(result)
    #if(internal == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] or [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]):
    #    print("found")
    print(internal)

if __name__ == "__main__":
    Main()