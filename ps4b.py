from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None
    # For each word in the wordList
    for word in wordList:
        

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):

            
            # Find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > max_score:
                # Update your best score, and best word accordingly
                max_score = score
                best_word = word

    # return the best word you found.
    return best_word

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    score = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
           
        # Display the hand
        print 'Current Hand:',
        displayHand(hand)
        # Ask user for input
        word  = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        else:        
            # If the word is not valid:
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            word_score = 0
            word_score = getWordScore(word, n)
            score += word_score
            print '"%s" earned %s points. Total: %s points'%(word, word_score, score)
            print ''
            # Update the hand 
            hand = updateHand(hand, word)

    
    print 'Total score:', score, 'points.'
    print 
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    #print "playGame not yet implemented." # <-- Remove this when you code this function
    player_option = None
    player_hand = None
    play_command = None
    while player_option != 'e':
        player_option = raw_input("Enter n to deal a new hand, r to replay the" +
                                  "  last hand, or e to end game: ")
        if player_option == 'n':
            player_hand = dealHand(HAND_SIZE)
            while True:
                play_command = raw_input('Enter u for the user to play the hand, or c for the computer to play the hand: ')
                if play_command == 'u':
                        playHand(player_hand.copy(), wordList, HAND_SIZE)
                        break
                elif play_command == 'c':
                        compPlayHand(player_hand.copy(), wordList)
                        break
                else:
                        print "Invalid command."
            
        elif player_option == 'r':
                if player_hand != None:
                    
                    play_command = raw_input('Enter u for the user to play the hand, or c for the computer to play the hand: ')
                    if play_command == 'u':
                        playHand(player_hand.copy(), wordList, n)
                        break
                    elif play_command == 'c':
                        compPlayHand(player_hand.copy(), wordList)
                        break
                    else:
                        print "Invalid command."
                    
                else:
                        print("You ve not played a hand yet. Please play a" +
                      " new hand first!\n")
                      
        elif player_option != 'e':
                            print("Invalid command.")


        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
    
    compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)


