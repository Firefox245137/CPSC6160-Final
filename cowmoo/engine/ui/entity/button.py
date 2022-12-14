import random

class Button: 
    def __init__(self, bounds=(0,0,10,20), color=(128, 128, 128), name="button"): 
        self.bounds = bounds 
        self.color = color            # (r,g,b) 
        self.template = None          # Member variable for the image template in a template button 
        self.actions = [] 
        self.name = name 
        self.verbose = False 
        self.active = True 
        return 
 
    def insert_action(self, a): 
        a.entity_state = self 
        self.actions.append(a) 
        return 

 
    # Check whether a position is inside the bounds 
    def is_inside( self, pos): 
        if pos[0] < self.bounds[0]: 
            return False 
        if pos[0] > self.bounds[2] + self.bounds[0]: 
            return False 
        if pos[1] < self.bounds[1]: 
            return False 
        if pos[1] > self.bounds[3] + self.bounds[1]: 
            return False 
        return True 
 
 