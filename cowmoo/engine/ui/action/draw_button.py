import pygame 
 
class DrawButton: 
    def __init__(self): 
        self.types = ["display"] 
        self.entity_state = None 
        self.verbose = False 
        self.name = "draw_button" 
        self.children = []
        self.size = 32
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
        fontObj = pygame.font.Font('freesansbold.ttf', self.size)
        textSurfaceObj = fontObj.render(self.entity_state.message, True, (0, 0, 0, 255), self.entity_state.color)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (self.entity_state.bounds[0] + (self.entity_state.bounds[2]/2), self.entity_state.bounds[1] + (self.entity_state.bounds[3]/2))
        screen.blit(textSurfaceObj, textRectObj)
        return 
