def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    y = 0
    g = 0
    
    #if x > b:
    if x == 1:
        return b        
    while y < x:
        y = pow(b,g)
        if y <= x:
            g = g + 1
    return g - 1
       
result = myLog(16, 2)                        
print result
        
            
   
