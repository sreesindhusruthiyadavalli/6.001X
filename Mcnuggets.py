def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    #sol = False
    if (n < 6): 
        return False
    if (n % 6 == 0)or(n % 9 == 0)or(n % 20 == 0):
        return True 
    if n > 20 and n % 3 != 0: 
        return McNuggets(n - 20) 
    if  n > 9: 
        return McNuggets(n - 9) 
    if n > 6: 
        return McNuggets(n - 6) 
    return False

print McNuggets(39)
