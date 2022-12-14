import pygame

class OutsideRectangleCollider: 
    def __init__(self): 
        self.types = ["physics"]                 # one or more types to assign to this action 
                                               # the specific types “event”, “loop”, “display” 
                                               # are picked up and used by the game looper. 
                                               # Any other types are for your organization convenience. 
        self.entity_state = None               # This class variable is assigned by the entity’s insert_action call 
        self.name = "outside_rectangle_collider"          # Names are frequently useful 
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
            for i in range(0, len(data.acceleration)):
                if data.active_particle[i]:
                    if data.position[i][0] > self.entity_state.llc[0] and data.position[i][0] < self.entity_state.urc[0] and data.position[i][1] > self.entity_state.llc[1] and data.position[i][1] < self.entity_state.urc[1]:
                        right_time = (data.position[i][0] - self.entity_state.llc[0])/data.velocity[i][0]
                        if right_time < 0:
                            right_time = 10000000.0
                        left_time = (data.position[i][0] - self.entity_state.urc[0])/data.velocity[i][0]
                        if left_time < 0:
                            left_time = 10000000.0
                        top_time = (data.position[i][1] - self.entity_state.llc[1])/data.velocity[i][1]
                        if top_time < 0:
                            top_time = 10000000.0
                        bottom_time = (data.position[i][1] - self.entity_state.urc[1])/data.velocity[i][1]
                        if bottom_time < 0:
                            bottom_time = 10000000.0
                        min_time = min(right_time, left_time, top_time, bottom_time)
                        if right_time == min_time:
                            data.position[i][0] = 2.0 * self.entity_state.llc[0] - data.position[i][0]
                            data.velocity[i][0] *= -1.0
                        elif left_time == min_time:
                            data.position[i][0] = 2.0 * self.entity_state.urc[0] - data.position[i][0]
                            data.velocity[i][0] *= -1.0
                        elif top_time == min_time:
                            data.position[i][1] = 2.0 * self.entity_state.llc[1] - data.position[i][1]
                            data.velocity[i][1] *= -1.0
                        else:
                            data.position[i][1] = 2.0 * self.entity_state.urc[1] - data.position[i][1]
                            data.velocity[i][1] *= -1.0
            for c in self.children:            # Have the children act as well 
                c.act(data) 
            if self.verbose:                   # A diagnostic when the verbose is True 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return