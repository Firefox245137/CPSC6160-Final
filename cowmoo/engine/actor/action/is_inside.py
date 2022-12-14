import pygame

class IsInside: 
    def __init__(self, offset=0): 
        self.types = []                 # one or more types to assign to this action 
                                               # the specific types “event”, “loop”, “display” 
                                               # are picked up and used by the game looper. 
                                               # Any other types are for your organization convenience. 
 
        self.entity_state = None               # This class variable is assigned by the entity’s insert_action call 
        self.to_check = []                     # Theorhetically can check multiple different particles classes
        self.offset = offset
        self.name = "is_inside"                # Names are frequently useful 
        self.verbose = False                   # verbose flags are handy 
        self.children = []                     # List of child actions that this action may choose to call 
 
    def condition_to_act(self, data):          # Check whether conditions are right for running this action 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False  
        if len(self.to_check) < 1:
            return False
        return True 
 
    def act(self, data):                       # Run this action if the conditions are right 
        if self.condition_to_act(data):        # Check whether the conditions are right 
            new_data = []
            curr = 0
            for i in self.to_check:
                for p in i.position:
                    if p[0] > self.entity_state.bounds[0]-self.offset and p[0] < self.entity_state.bounds[2] + self.entity_state.bounds[0]+self.offset and p[1] > self.entity_state.bounds[1]-self.offset and p[1] < self.entity_state.bounds[3] + self.entity_state.bounds[1]+self.offset: 
                        new_data.append(curr)
                        print("inside")
                    curr += 1
            for i in new_data:
                for c in self.children:            # Have the children act as well 
                    c.act(i) 
            if self.verbose:                   # A diagnostic when the verbose is True 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return