import pygame

class clear():
	
	def __init__(self):
		self.types = ["clear"] #  assign as event
		self.entity_state = None # This class variable is assigned by the entity’s insert_action call
		self.name = "terminate_event" # action's name
		self.verbose = False # verbose flags are handy
		self.children = [] # List of child actions that this action may choose to call
		
	def act(self,data):
		print(">>>clear content")	
		#del self.entity_state.game_content[:]
		del self.entity_state.display_content[1:]
		del self.entity_state.event_content[1:]
		#del self.entity_state.loop_content[:]
		
		#print("display_content = " + str(self.entity_state.display_content))
		#print("event_content = " + str(self.entity_state.event_content))
