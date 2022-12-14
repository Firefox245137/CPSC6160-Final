import pygame

class EulerSolve: 
    def __init__(self): 
        self.types = ["physics"]                 # one or more types to assign to this action 
                                               # the specific types “event”, “loop”, “display” 
                                               # are picked up and used by the game looper. 
                                               # Any other types are for your organization convenience. 
        self.dt = 1.0
        self.entity_state = None               # This class variable is assigned by the entity’s insert_action call 
        self.name = "euler_solve"          # Names are frequently useful 
        self.verbose = False                   # verbose flags are handy 
        self.children = []                     # List of child actions that this action may choose to call 
 
    def condition_to_act(self, data):          # Check whether conditions are right for running this action 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False  
        if len(self.children) < 2:
            return False
        return True 
 
    def act(self, data):                      # Run this action if the conditions are right 
        if self.condition_to_act(data):        # Check whether the conditions are right 
            # print(self.entity_state.position[0])
            self.children[0].dt = float(self.dt)
            self.children[1].dt = float(self.dt)
            self.children[0].act(data)
            self.children[1].act(data)
            for c in self.children[2:]:            # Have the children act as well 
                c.act(data) 
            if self.verbose:                   # A diagnostic when the verbose is True 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return