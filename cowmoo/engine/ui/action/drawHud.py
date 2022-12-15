import pygame

class DrawHudAction():
	def __init__(self):
		self.types = ["display"] # assign as display action
		self.entity_state = None # This class variable is assigned by the entity’s insert_action call
		self.verbose = False # verbose flags are handy 
		self.name = "draw_hud_action" # action's name
		#self.fontObj = pygame.font.Font('freesansbold.ttf', 16) # init text font
		self.children = [] # List of child actions that this action may choose to call
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
			#print("drawHub: " + self.entity_state.message)
			self.draw(data)
		if self.verbose:
			print(self.name + " for " + self.entity_state.name)
		return			
			
	def draw(self, screen): # draw the letter
		fontObj = pygame.font.Font('freesansbold.ttf', self.entity_state.size)
		textSurfaceObj = fontObj.render(self.entity_state.message, True, self.entity_state.msgColor, self.entity_state.backgroundColor)
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (self.entity_state.xpos, self.entity_state.ypos)
		screen.blit(textSurfaceObj, textRectObj)
		return
