
class LoadLevel:
    def __init__(self, levelName, gameLoop, displayMaster):
        self.types = []
        self.entity_state = None               # This class variable is assigned by the entity’s insert_action call 
        self.name = "load_level"          # Names are frequently useful 
        self.verbose = False                   # verbose flags are handy 
        self.levelName = "../../cowmoo/python/" + levelName + ".py"       #This assumes all the levels are in a 'python' folder
        self.pureName = levelName
        self.gameLoop = gameLoop                #The game looper
        self.displayMaster = displayMaster      #The updateDisplay function
        self.children = []                     # List of child actions that this action may choose to call 
 
    #LoadLevel is a special Action that we didn't want bound to an entity so it has no conditions
    def condition_to_act(self, data):          # Check whether conditions are right for running this action 
        # if self.entity_state == None: 
        #     return False 
        # if self.entity_state.active == False: 
        #     return False  
        return True 
 
    def act(self, data):                       # Run this action if the conditions are right 
        if self.condition_to_act(data):        # Check whether the conditions are right 
            # for a in self.gameLoop.loop_content:
            #     del a
            #First, clear all the current level content
            #Originally this was going to be a seperate Action, but when we thought about it: there's literally no reason to load a level without first clearing the last one, so clear is in here now
            self.displayMaster.children.clear()
            term = self.gameLoop.event_content[0]
            self.gameLoop.event_content.clear()
            self.gameLoop.display_content.clear()
            self.gameLoop.loop_content.clear()
            self.gameLoop.event_content.append(term)
            self.gameLoop.display_content.append(self.displayMaster)
            
            #LoadLevel uses exec() to load in a new level
            #The levels are stored in seperate python files (the level names can technically be whatever you want but for our game we made them all "levelX.py")
            lvl = open(self.levelName, "r")
            
            #Variables to pass down to the "level" file
            entities = []
            displayActions = []
            gloop = self.gameLoop
            dplay = self.displayMaster
            
            #Run exec() / This is equivalent to just having all the code in the (for example) "level1.py" file pasted right here, but this way it's modular and not game dependent
            exec(lvl.read())
            
            #After the level file is done creating all its entities and drawActions, load them into the real gameLoop and updateFunction
            for e in entities:
                self.gameLoop.insert_entity(e)
            for d in displayActions:
                self.displayMaster.children.append(d)
                
            #Close file
            lvl.close()
            for c in self.children:            # Have the children act as well 
                c.act(data) 
            if self.verbose:                   # A diagnostic when the verbose is True 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return