from pygame.locals import * 
 
class PressButton: 
    def __init__(self): 
        self.types = ["event"] 
        self.entity_state = None 
        self.name = "button_pressed" 
        self.verbose = False
        self.children = [] 
 
    def condition_to_act(self, event): 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False 
        if event.type == MOUSEBUTTONDOWN: 
            # check whether the mouse button is down inside the button area 
            pos = event.pos 
            return self.entity_state.is_inside(pos) 
        return False 
 
    def act(self, event): 
        if self.condition_to_act(event): 
            for c in self.children: 
                c.act(event)
            if self.verbose: 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return  