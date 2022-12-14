import pygame

class RectangleCollider: 
    def __init__(self, llc = [0.0,0.0], urc = [10.0,10.0], name="rect_collider"): 
        self.llc = llc
        self.urc = urc
        self.actions = []          # The actions that dictate what happens with this entity 
        self.name = name         # Names are handy for diagnostics and tracking 
        self.verbose = False       # Useful for deciding to show info or not 
        self.active = True        # Decide whether or not you want this entity to be active 
        self.isTrigger = False
        return 
 
    def insert_action(self, a):    # append an input action to the self.actions list,  
                                   # and set the input actions entity_state to this entity 
        a.entity_state = self 
        self.actions.append(a) 
        return 

