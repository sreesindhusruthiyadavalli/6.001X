def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    if isMyNumber(guess) == 0:
        return guess
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        if sign == -1:
            guess *= 2
        else:
            guess -= 1
            if isMyNumber(guess) == 0:
                return guess
    return guess

    
def isMyNumber(guess):
    secret_number = 10
    if secret_number == guess:
        return 0
    elif secret_number < guess:
        return 1
    elif secret_number > guess:
        return -1              
    
isMyNumber = 10
print jumpAndBackpedal(isMyNumber)  
