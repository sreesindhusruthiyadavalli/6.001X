class Queue(object):
    def __init__(self):
        self.vals = []
        
    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        self.vals.append(e)    
    
    def remove(self):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        
        if self.vals == []:
            raise ValueError()
        else:
            return self.vals.pop(0)  
    
