def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    middle = len(aStr)/2
    if aStr == '':
        return False
    if len(aStr) == 1:
        return char == aStr
            
    if char == aStr[middle]:
        return True
    elif  char < aStr[middle]:
        return isIn(char,aStr[0:middle])
    else:
        return isIn(char,aStr[middle:])
        
    """# Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character 
   midIndex = len(aStr)/2
   midChar = aStr[midIndex]
   if char == midChar:
      # We found the character!
      return True
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
   elif char < midChar:
      return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn(char, aStr[midIndex:])"""
               
 
x = isIn('e', "abcdef")   
print x                                                      
        
