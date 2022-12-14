class DeactivatePhysics: 
    def __init__(self, forces): 
        self.types = []                 # one or more types to assign to this action 
                                               # the specific types “event”, “loop”, “display” 
                                               # are picked up and used by the game looper. 
                                               # Any other types are for your organization convenience.
        self.forces = forces
        self.entity_state = None               # This class variable is assigned by the entity’s insert_action call 
        self.name = "deactivate_physics"    # Names are frequently useful 
        self.verbose = False                   # verbose flags are handy 
        self.children = []                     # List of child actions that this action may choose to call 
 
    def condition_to_act(self, data):          # Check whether conditions are right for running this action 
        if self.entity_state == None: 
            return False         
        return True 
 
    def act(self, data):                       # Run this action if the conditions are right 
        if self.condition_to_act(data):        # Check whether the conditions are right 
            if "active" in self.forces:
                self.entity_state.active_particle[data] = False
            if "gravity" in self.forces:
                self.entity_state.active_gravity[data] = False
            if "spring" in self.forces:
                self.entity_state.active_spring[data] = False
            if "drag" in self.forces:
                self.entity_state.active_drag[data] = False
            for c in self.children:            # Have the children act as well 
                c.act(data) 
            if self.verbose:                   # A diagnostic when the verbose is True 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return