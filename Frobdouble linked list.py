def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    # Your Code Here
    if atMe.myName() < newFrob.myName():
        if atMe.getAfter()==None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        else:
            tempFrob = atMe.getAfter()
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
            newFrob.setAfter(tempFrob)
            tempFrob.setBefore(newFrob)
    else:
        if atMe.getBefore()==None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        else:
            tempFrob = atMe.getBefore()
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
            newFrob.setBefore(tempFrob)
            tempFrob.setAfter(newFrob)
