# import cowmoo.engine.play.action.Ter

class LoadLevel:
    def __init__(self, levelName, gameLoop, displayMaster):
        self.types = []
        self.entity_state = None               # This class variable is assigned by the entity’s insert_action call 
        self.name = "load_level"          # Names are frequently useful 
        self.verbose = False                   # verbose flags are handy 
        self.levelName = "../../cowmoo/python/" + levelName + ".py"       #This assumes all the levels are in a 'python' folder
        self.gameLoop = gameLoop
        self.displayMaster = displayMaster
        self.children = []                     # List of child actions that this action may choose to call 
 
    def condition_to_act(self, data):          # Check whether conditions are right for running this action 
        # if self.entity_state == None: 
        #     return False 
        # if self.entity_state.active == False: 
        #     return False  
        # if pygame.key.get_pressed()[self.key]:
        #     return True
        return True 
 
    def act(self, data):                       # Run this action if the conditions are right 
        if self.condition_to_act(data):        # Check whether the conditions are right 
            for a in self.gameLoop.loop_content:
                if(a.__class__.__name__ == "UpdateTimer"):
                    print("Time taken for level:", a.entity_state.elapsed_time()/1000)
                del a
            self.displayMaster.children.clear()
            term = self.gameLoop.event_content[0]
            self.gameLoop.event_content.clear()
            self.gameLoop.display_content.clear()
            self.gameLoop.loop_content.clear()
            self.gameLoop.event_content.append(term)
            self.gameLoop.display_content.append(self.displayMaster)
            # print(self.gameLoop.loop_content)
            lvl = open(self.levelName, "r")
            entities = []
            displayActions = []
            gloop = self.gameLoop
            dplay = self.displayMaster
            exec(lvl.read())
            # print(entities)
            for e in entities:
                self.gameLoop.insert_entity(e)
            for d in displayActions:
                self.displayMaster.children.append(d)
            # print(self.gameLoop.loop_content)
            lvl.close()
            for c in self.children:            # Have the children act as well 
                c.act(data) 
            if self.verbose:                   # A diagnostic when the verbose is True 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return