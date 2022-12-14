import pygame

class Particles: 
    def __init__(self, name="particles"): 
        self.position = []
        self.velocity = []
        self.acceleration = []
        self.mass = []
        self.active_particle = []
        self.active_gravity = []
        self.active_spring = []
        self.active_drag = []
        self.actions = []          # The actions that dictate what happens with this entity 
        self.name = name         # Names are handy for diagnostics and tracking 
        self.verbose = False       # Useful for deciding to show info or not 
        self.active = True        # Decide whether or not you want this entity to be active 
        return 
 
    def insert_action(self, a):    # append an input action to the self.actions list,  
                                   # and set the input actions entity_state to this entity 
        a.entity_state = self 
        self.actions.append(a) 
        return 

    def add_particle(self, p, v, m):
        self.position.append(p)
        self.velocity.append(v)
        self.acceleration.append([0.0, 0.0])
        self.mass.append(m)
        self.active_particle.append(True)
        self.active_gravity.append(True)
        self.active_spring.append(True)
        self.active_drag.append(True)

