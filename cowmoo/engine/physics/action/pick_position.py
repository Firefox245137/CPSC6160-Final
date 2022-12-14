import pygame

class PickPosition: 
    def __init__(self, index): 
        self.types = ["position"]                 # one or more types to assign to this action 
                                               # the specific types “event”, “loop”, “display” 
                                               # are picked up and used by the game looper. 
                                               # Any other types are for your organization convenience. 
        self.particle_index = index
        self.entity_state = None               # This class variable is assigned by the entity’s insert_action call 
        self.name = "pick_position"          # Names are frequently useful 
        self.verbose = False                   # verbose flags are handy 
        self.children = []                     # List of child actions that this action may choose to call 
 
    def condition_to_act(self, data):          # Check whether conditions are right for running this action 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False  
        if self.particle_index >= len(self.entity_state.position):
            return False
        if self.entity_state.active_particle[self.particle_index] == False:
            return False
        return True 
 
    def act(self, data):                       # Run this action if the conditions are right 
        if self.condition_to_act(data):        # Check whether the conditions are right 
            new_data = list(self.entity_state.position[self.particle_index])
            for c in self.children:            # Have the children act as well 
                c.act(new_data) 
            if self.verbose:                   # A diagnostic when the verbose is True 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return