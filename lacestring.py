def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    #str3 = ''
    """if len(s1) == len(s2):
        for x, y in zip(s1,s2) :
            str3 = str3 + s1[x] + s2[y]
                
    if(len(s1)<len(s2)):
        sl = s1
        gl = s2
    else:
        sl = s2
        gl = s1
    for i in range(0,len(sl)):
        str3 = str3 + s1[i]
        str3 = str3 + s2[i]
    str3 += ll[len(sl):]
    return str3"""
    length = min(len(s1), len(s2))
    str3 = ""
    for i in range(length):
        if len(s1) >= 1:
            str3 += s1[0]
            s1 = s1[1:]
        else:
            s1 = ""
        if len(s2) >= 1:
            str3 += s2[0]
            s2 = s2[1:]
        else:
            s2 = ""
    str3 += s1 + s2
    return str3
                
            
    
s1 = 'abcdefgh'
s2 = 'x'
result = laceStrings(s1, s2)           
print result
