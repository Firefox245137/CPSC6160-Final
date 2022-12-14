import pygame

class Rectangle: 
    def __init__(self, bounds=(0,0,10,10), color=(255,255,255), name="rect"): 
        self.tags = []
        self.color = color
        self.bounds = bounds
        self.actions = []          # The actions that dictate what happens with this entity 
        self.name = name          # Names are handy for diagnostics and tracking 
        self.verbose = False       # Useful for deciding to show info or not 
        self.active = True        # Decide whether or not you want this entity to be active 
        return 
 
    def insert_action(self, a):    # append an input action to the self.actions list,  
                                   # and set the input actions entity_state to this entity 
        a.entity_state = self 
        self.actions.append(a) 
        return 
    
    def move(self, x, y):
        self.bounds = (self.bounds[0]+x, self.bounds[1]+y, self.bounds[2], self.bounds[3])