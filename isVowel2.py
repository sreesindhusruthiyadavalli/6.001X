def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    return bool('a' in char or 'e' in char or 'i' in char or 'o' in char\
                 or 'u' in char or 'A' in char or 'E' in char or 'I' in char\
                 or 'O' in char or 'U'in char)
