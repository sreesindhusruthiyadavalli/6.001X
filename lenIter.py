def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    #return sum(c) for c in aStr)
    count = 0
    for char in aStr:
        count += 1
    return count
        
        
x = lenIter("twenty")
print x
