import pygame

class VelocitySolve: 
    def __init__(self): 
        self.types = ["physics"]                 # one or more types to assign to this action 
                                               # the specific types “event”, “loop”, “display” 
                                               # are picked up and used by the game looper. 
                                               # Any other types are for your organization convenience. 
        self.dt = 1.0
        self.entity_state = None               # This class variable is assigned by the entity’s insert_action call 
        self.name = "velocity_solve"          # Names are frequently useful 
        self.verbose = False                   # verbose flags are handy 
        self.children = []                     # List of child actions that this action may choose to call 
 
    def condition_to_act(self, data):          # Check whether conditions are right for running this action 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False  
        return True 
 
    def act(self, data):                       # Run this action if the conditions are right 
        if self.condition_to_act(data):        # Check whether the conditions are right 
            for i in range(len(self.entity_state.acceleration)):
                if(self.entity_state.active_particle[i]):
                    self.entity_state.acceleration[i][0] = 0.0
                    self.entity_state.acceleration[i][1] = 0.0
            for c in self.children:            # Have the children act as well 
                c.act(self.entity_state) 
            for i in range(len(self.entity_state.velocity)):
                if(self.entity_state.active_particle[i]):
                    # print(self.dt * self.entity_state.acceleration[i][1] + self.entity_state.velocity[i][1])
                    self.entity_state.velocity[i][0] += self.dt * self.entity_state.acceleration[i][0]
                    self.entity_state.velocity[i][1] += self.dt * self.entity_state.acceleration[i][1]
            if self.verbose:                   # A diagnostic when the verbose is True 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return