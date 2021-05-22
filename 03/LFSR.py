####
# This program implements a LFSR
####


def Init():
    ## Init with 0x1FFFFF = 111111111111111111111
    flops_len = 21
    flops_array = [1]*flops_len
    out_array = []
    temp_flops = flops_array.copy()

    for n in range(0, 64):

        temp_flops = flops_array.copy()
        
        for x in range(flops_len-1, -1, -1):
            #print("array: ", flops_array, "x: ", x)
            if(x-1 >= 0):
                flops_array[x-1] = temp_flops[x]
            else:
                flops_array[flops_len-1] = (temp_flops[0]^temp_flops[2])
                
                #flops_array[flops_len-1] = (flops_array[0]^flops_array[2])^flops_array[flops_len-1]
                #print(flops_array[flops_len-1])
                #print(flops_array[0]^flops_array[2])
                #print((flops_array[0]^flops_array[2])^flops_array[flops_len-1])

        out_array.append(flops_array[0])

    return out_array
    
def Main():
    #print(Init())
    sol = Init()
    my_solution = "".join(str(e) for e in sol)
    print(my_solution)
    solution = "1111111111111111111110011001100110011001101001011010010110100100"

    if(my_solution == solution):
        print("success")
        
if __name__ == "__main__":
    Main()