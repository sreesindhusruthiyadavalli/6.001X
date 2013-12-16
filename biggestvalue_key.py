def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    k = aDict.keys()
    result = None
    
    maxvalue = 0
    for l in k:
        if len(aDict[l]) >= maxvalue:
            result = l
            maxvalue = len(aDict[l])
    return result   

         
    
