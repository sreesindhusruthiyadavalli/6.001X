# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    """if atMe.myName() < newFrob.myName():
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
            tempFrob.setAfter(newFrob)"""
    if newFrob.myName() <= atMe.myName() :
        
        # set atMe's before object
        
        # test existence of a before object
        if atMe.getBefore() == None :
            # if not existing, set newFrob as the new linked object
            atMe.setBefore(newFrob)
        else :
            # if newFrob is after atMe's before
            if newFrob.myName() >= atMe.getBefore().myName() :
                atMe.getBefore().setAfter(newFrob)
                newFrob.setBefore(atMe.getBefore())
                newFrob.setAfter(atMe)
                atMe.setBefore(newFrob)
            else :
                currentFrob = atMe
                while newFrob.myName() < currentFrob.getBefore().myName() :
                    currentFrob = currentFrob.getBefore()
                currentFrob.getBefore().setAfter(newFrob)
                newFrob.setBefore(currentFrob.getBefore())
                newFrob.setAfter(currentFrob)
                currentFrob.setBefore(newFrob)
                
        # set newFrob's after object
                
        if newFrob.getAfter() == None :
            newFrob.setAfter(atMe)
            
        
        
    # if newFrob is after atMe
    if newFrob.myName() >= atMe.myName() :
        
        # set atMe's after object
        
        # test existence of an after object
        if atMe.getAfter() == None :
            # if not existing, set newFrob as the new linked object
            atMe.setAfter(newFrob)
        else :
            # if newFrob is before atMe's after
            if newFrob.myName() <= atMe.getAfter().myName() :
                atMe.getAfter().setBefore(newFrob)
                newFrob.setAfter(atMe.getAfter())
                newFrob.setBefore(atMe)
                atMe.setAfter(newFrob)
            else :
                currentFrob = atMe
                while newFrob.myName() > currentFrob.getAfter().myName() :
                    currentFrob = currentFrob.getAfter()
                currentFrob.getAfter().setBefore(newFrob)
                newFrob.setAfter(currentFrob.getAfter())
                newFrob.setBefore(currentFrob)
                currentFrob.setAfter(newFrob)
                
        # set newFrob's before object
                
        if newFrob.getBefore() == None :
            newFrob.setBefore(atMe)
    
    
                    
            
                
