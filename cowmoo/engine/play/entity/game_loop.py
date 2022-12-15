import pygame

class GameLoop: 
    def __init__(self, name="game_looper"): 
        self.tags = []
        self.loop_content = []
        self.event_content = []
        self.display_content = []
        self.actions = []          # The actions that dictate what happens with this entity 
        self.name = name          # Names are handy for diagnostics and tracking 
        self.verbose = False       # Useful for deciding to show info or not 
        self.active = True        # Decide whether or not you want this entity to be active 
        return 
 
    def insert_entity(self, e):
        if(self.verbose):
            print("Inserting entity " + e.name)
        for a in e.actions:
            self.insert_action(a)
        return

    def insert_action(self, a):    # append an input action to the self.actions list,  
                                   # and set the input actions entity_state to this entity 
        if "event" in a.types:
            self.event_content.append(a)
            a.loop_entity = self
            if(self.verbose):
                print(self.name + " inserted action " + a.name)
        elif "display" in a.types:
            self.display_content.append(a)
            if(self.verbose):
                print(self.name + " inserted action " + a.name)
        elif "loop" in a.types:
            self.loop_content.append(a)
            if(self.verbose):
                print(self.name + " inserted action " + a.name)
        elif "clear" in a.types:
            a.entity_state = self
        return

    def loop(self):
        while self.active:
            events = pygame.event.get()
            for e in events:
                for a in self.event_content:
                    a.act(e)
            for a in self.loop_content:
                a.act(None)
            for a in self.display_content:
                a.act(None)
				
        return
