class Counter: 
    def __init__(self, name="counter"): 
        self.actions = []          # The actions that dictate what happens with this entity 
        self.name = name          # Names are handy for diagnostics and tracking 
        self.verbose = False       # Useful for deciding to show info or not 
        self.active = True        # Decide whether or not you want this entity to be active 
        self.counter_value = 0
        return 
 
    def insert_action(self, a):    # append an input action to the self.actions list,  
                                   # and set the input actions entity_state to this entity 
        a.entity_state = self 
        self.actions.append(a) 
        return 
 