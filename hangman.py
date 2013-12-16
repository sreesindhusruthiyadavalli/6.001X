def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is", str(len(secretWord)), "letters long."
    print "-------------"
    guessLeft=8
    lettersGuessed=[]
    while guessLeft>0 and not isWordGuessed(secretWord, lettersGuessed):
            print "You have",str(guessLeft),"guesses left."
            print "Available letters:",getAvailableLetters(lettersGuessed)
            guess=str(raw_input("Please guess a letter: "))
            guess=guess.lower()
            while len(guess)!=1 and guess not in string.ascii_lowercase:
                    guess=str(raw_input("Please guess a letter: "))
            if guess not in lettersGuessed:
                    lettersGuessed.append(guess)
                    if guess in secretWord:
                            print "Good guess:",
                    else:
                            guessLeft-=1
                            print "Oops! That letter is not in my word:",
            else:
                    print "Oops! You've already guessed that letter:",
            print getGuessedWord(secretWord, lettersGuessed)
            print "------------"
    if isWordGuessed(secretWord, lettersGuessed):
            print "Congratulations, you won!"
    else:
            print "Sorry, you ran out of guesses. The word was", str(secretWord)
