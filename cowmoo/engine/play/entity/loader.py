import pygame
import cowmoo.engine.play as pl 

class Loader: 
    def __init__(self, game_looper, timer): 
        self.display = pl.make_update_display_action()
        self.entity = []
        self.actions = []          # The actions that dictate what happens with this entity 
        self.name = "loader"          # Names are handy for diagnostics and tracking 
        self.verbose = False       # Useful for deciding to show info or not 
        self.active = True        # Decide whether or not you want this entity to be active 
        self.level = 0
        self.gameLoop = game_looper
        self.timer = timer
        return 
 
    def insert_action(self, a):    # append an input action to the self.actions list,  
                                   # and set the input actions entity_state to this entity 
        a.entity_state = self 
        self.actions.append(a) 
        return 
