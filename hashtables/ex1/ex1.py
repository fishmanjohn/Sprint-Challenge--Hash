from hashtable import (Hashtable, get, put) 

def get_indices_of_item_weights(weights, length, limit):
    #initalize hashtable with size
    ht = Hashtable(16)
    #
    for i in range(0, len(weights)):
        #checks value of limit - weights for each  
        value = get(ht, limit - weights[i])
        if value != None:
            #if limit and weight cancel eachother out
            return (i, value)
        else:
            #adds weights and indexes to hashtable
            put(ht, weights[i], i)

    return None
