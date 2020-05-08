from hashtable import (Hashtable, get, put) 

def get_indices_of_item_weights(weights, length, limit):
    ht = Hashtable(16)
    for i in range(0, len(weights)):
        
        value = get(ht, limit - weights[i])
        if value != None:
            return (i, value)
        else:
            put(ht, weights[i], i)

    return None
