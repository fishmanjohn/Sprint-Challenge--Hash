class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Hashtable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

def hash(x, max):
    x = ((x >> 16) ^ x) * 0x45d9f3b
    x = ((x >> 16) ^ x) * 0x45d9f3b
    x = ((x >> 16) ^ x)

    return x % max

def put(hash_table, key, value):
    index = hash(key, len(hash_table.storage))

    current_pair = hash_table.storage[index]
    last_pair = None

    while current_pair is not None and current_pair.key != key:
        last_pair = current_pair
        current_pair = last_pair.next

    if current_pair is not None:
        current_pair.value = value
    else:
        new_pair = HashTableEntry(key, value)
        new_pair.next = hash_table.storage[index]
        hash_table.storage[index] = new_pair

def delete(hash_table, key):
    index = hash(key, len(hash_table.storage))

    current_pair = hash_table.storage[index]
    last_pair = None

    while current_pair is not None and current_pair.key != key:
        last_pair = current_pair
        current_pair = last_pair.next

    if current_pair is None:
        print("ERROR: Unable to remove entry with key " + key)
    else:
        if last_pair is None:  # Removing the first element in the LL
            hash_table.storage[index] = current_pair.next
        else:
            last_pair.next = current_pair.next
    

def get(hash_table, key):
    index = hash(key, len(hash_table.storage))

    current_pair = hash_table.storage[index]

    while current_pair is not None:
        if(current_pair.key == key):
            return current_pair.value
        current_pair = current_pair.next


def resize(hash_table):
    new_hash_table = HashTable(2 * len(hash_table.storage))

    current_pair = None

    for i in range(len(hash_table.storage)):
        current_pair = hash_table.storage[i]
        while current_pair is not None:
            hash_table_insert(new_hash_table,
                            current_pair.key,
                            current_pair.value)
            current_pair = current_pair.next

    return new_hash_table