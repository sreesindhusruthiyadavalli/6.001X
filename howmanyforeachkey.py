

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    k = aDict.keys()
    length = 0
    for l in k:
        length = length + len(aDict[l]) 
    return length    
    
   
        
    
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

value = howMany(animals)
print value
