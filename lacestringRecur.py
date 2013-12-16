def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            #PLACE A LINE OF CODE HERE
            return s2
        if s2 == '':
            #PLACE A LINE OF CODE HERE
            return s1
        else:
            #PLACE A LINE OF CODE HERE
            return out + s1[0] + s2[0] + laceStringsRecur(s1[1:], s2[1:]) 
    return helpLaceStrings(s1, s2, '')
    
s1 = 'a'
s2 = 'jklmnopqrs'
result = laceStringsRecur(s1, s2)           
print result    

"""print "axbycz? " + laceStrings("abc", "xyz")
print "axbyz? " + laceStrings("ab", "xyz")
print "axbyc? " + laceStrings("abc", "xy")
print "axbcdefgh? " + laceStrings("abcdefgh", "x") 
print "ajklmnopqrs? " + laceStrings("a", "jklmnopqrs")
 """
