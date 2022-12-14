import pygame

class FrameViewer: 
    def __init__(self, width=500, height=500, name="frame_viewer"): 
        # pygame.font.init()
        # pygame.mixer.init()
        pygame.init()
        self.tags = []
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.window.fill((255,255,255))
        self.actions = []          # The actions that dictate what happens with this entity 
        self.name = name          # Names are handy for diagnostics and tracking 
        self.verbose = False       # Useful for deciding to show info or not 
        self.active = True        # Decide whether or not you want this entity to be active 
        return 
 
    def insert_action(self, a):    # append an input action to the self.actions list,  
                                   # and set the input actions entity_state to this entity 
        a.entity_state = self 
        self.actions.append(a) 
        return 

    def set_title(self, title):
        pygame.display.set_caption(title)
        return

    def set_mode(self, width, height):
        self.window = pygame.display.set_mode((width, height))
        return