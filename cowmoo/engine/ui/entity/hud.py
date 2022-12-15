#
# basic hud
#
class Hud:
	def __init__(self, x, y, message, color, bkcolor, name="hud", size = 16): #hud.message = changed \n
		self.xpos = x #save letter's x position
		self.ypos = y #save letter's y position
		self.msgColor = color #save letter's color
		self.backgroundColor = bkcolor #save letter's background color
		self.message = message # Member variable for the message in a message button
		self.size = size
		self.actions = []
		self.name = name
		self.verbose = False
		self.active = True
		return
		
	def insert_action(self, action):
		action.entity_state = self
		self.actions.append(action)
		if self.verbose == True:
			print("letter: insert_action " + str(action) + str(self))
		return	
		
