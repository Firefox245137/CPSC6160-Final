import pygame

class SpringForceAction: 
    def __init__(self): 
        self.types = ["force"]                 # one or more types to assign to this action 
                                               # the specific types “event”, “loop”, “display” 
                                               # are picked up and used by the game looper. 
                                               # Any other types are for your organization convenience. 
        self.entity_state = None               # This class variable is assigned by the entity’s insert_action call 
        self.name = "spring_force_action"          # Names are frequently useful 
        self.verbose = False                   # verbose flags are handy 
        self.children = []                     # List of child actions that this action may choose to call 
 
    def condition_to_act(self, data):          # Check whether conditions are right for running this action 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False  
        if data == None:
            return False
        return True 
 
    def act(self, data):                       # Run this action if the conditions are right 
        if self.condition_to_act(data):        # Check whether the conditions are right 
            total_mass = 0.0
            center_mass = [0.0, 0.0]
            for i in range(0, len(data.acceleration)):
                if data.active_particle[i] and data.active_spring[i]:
                    total_mass += data.mass[i]
                    center_mass[0] += data.mass[i] * data.position[i][0]
                    center_mass[1] += data.mass[i] * data.position[i][1]
            center_mass[0] /= total_mass
            center_mass[1] /= total_mass

            for i in range(0, len(data.acceleration)):
                if data.active_particle[i] and data.active_spring[i]:
                    data.acceleration[i][0] += (center_mass[0] - data.position[i][0]) * self.entity_state.spring_constant / data.mass[i]
                    data.acceleration[i][1] += (center_mass[1] - data.position[i][1]) * self.entity_state.spring_constant / data.mass[i]
            for c in self.children:            # Have the children act as well 
                c.act(data) 
            if self.verbose:                   # A diagnostic when the verbose is True 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return