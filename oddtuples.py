def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    return aTup[0::2]
    
aTup = ('I', 'am', 'a', 'test', 'tuple')
value = oddTuples(aTup)
print value    
        
