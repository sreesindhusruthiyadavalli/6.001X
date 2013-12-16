def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
    #unequal strings
    if len(str1) != len(str2):
        return False
     #base case   
    if len(str1) == 1 or len(str2) == 1:
        return str1 == str2
    #semordnilap    
    if str1[0] == str2[-1]:
        return True and semordnilap(str1[1:],str2[:-1])
    else:
        return False        
    
        
x = semordnilap("dog","god") 
print x         
