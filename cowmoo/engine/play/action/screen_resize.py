import pygame

class ScreenResize: 
    def __init__(self): 
        self.types = ["event"]                 # one or more types to assign to this action 
                                               # the specific types “event”, “loop”, “display” 
                                               # are picked up and used by the game looper. 
                                               # Any other types are for your organization convenience. 
 
        self.entity_state = None               # This class variable is assigned by the entity’s insert_action call 
        self.name = "screen_resize"            # Names are frequently useful 
        self.verbose = False                   # verbose flags are handy 
        self.children = []                     # List of child actions that this action may choose to call 
 
    def condition_to_act(self, data):          # Check whether conditions are right for running this action 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False 
        if data.type == pygame.VIDEORESIZE:
            return True
        return False 
 
    def act(self, data):                       # Run this action if the conditions are right 
        if self.condition_to_act(data):        # Check whether the conditions are right 
            old = self.entity_state.window
            self.entity_state.window = pygame.display.set_mode((data.w, data.h), pygame.RESIZABLE)
            self.entity_state.window.blit(old, (0,0))
            del old
            self.entity_state.width = data.w
            self.entity_state.height = data.h
            for c in self.children:            # Have the children act as well 
                c.act(data) 
            if self.verbose:                   # A diagnostic when the verbose is True 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return