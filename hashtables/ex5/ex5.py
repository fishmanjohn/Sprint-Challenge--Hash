def finder(files, queries):
    # initilize a dictionary
    queire_dict = {}
    #make an array to append the results
    result = []
    #itterate over files 
    for f in files:
        # split the file path so that we get just the file name
        file_name = f.split("/")[-1]
        # add to dictionary 
        print(i)
    #at the same time itterate over quiries and check if that file is in is in the dictonary and if it is add it to results  
    #then return results 
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
