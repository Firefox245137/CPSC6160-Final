import pygame 
 
class DrawButton: 
    def __init__(self): 
        self.types = ["display"] 
        self.entity_state = None 
        self.verbose = False 
        self.name = "draw_button" 
        self.children = []
        return 
 
    def condition_to_act(self,data): 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False 
        if data == None: 
            return False 
        return True 
 
    def act(self,data): 
        if self.condition_to_act(data): 
            self.draw(data) 
            for c in self.children:            # Have the children act as well 
                c.act(data) 
            if self.verbose: 
                print(self.name + " for " + self.entity_state.name) 
        return 
 
    def draw(self, screen): 
        pygame.draw.rect(screen, self.entity_state.color, self.entity_state.bounds ) 
        return 