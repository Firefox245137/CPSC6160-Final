import pygame

import cowmoo.engine.play as pl 
import cowmoo.engine.ui as ui 
import cowmoo.engine.utility as util 
import cowmoo.engine.physics as phys
import cowmoo.engine.actor as act

WIDTH = 1280
HEIGHT = 720
playerWidth = 20
playerSpeed = 2.5
enemies = []
byLevel = []


RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
BLUE = (0, 0, 255, 255)
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)	
NONE = (0, 0, 0, 0)	

class EnemyAI:
    def __init__(self, direction, boundllc, boundurc):
        self.types = ["loop"]
        self.entity_state = None               # This class variable is assigned by the entity’s insert_action call 
        self.name = "enemy_AI"          # Names are frequently useful 
        self.verbose = False                   # verbose flags are handy 
        self.direction = direction
        self.boundllc = boundllc
        self.boundurc = boundurc
        self.children = []                     # List of child actions that this action may choose to call 
 
    def condition_to_act(self, data):          # Check whether conditions are right for running this action 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False  
        return True 
 
    def act(self, data):                       # Run this action if the conditions are right 
        if self.condition_to_act(data):        # Check whether the conditions are right 
            # print(data.key)
            # while()
            if self.boundllc[0] > self.entity_state.bounds[0] or self.boundllc[1] > self.entity_state.bounds[1] or self.boundurc[0] < self.entity_state.bounds[0] or self.boundurc[1] < self.entity_state.bounds[1]:
                self.direction[0] *= -1
                self.direction[1] *= -1
            self.entity_state.move(self.direction[0], self.direction[1])
            for c in self.children:            # Have the children act as well 
                c.act(data) 
            if self.verbose:                   # A diagnostic when the verbose is True 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return

class MovePlayer:
    def __init__(self, direction, key):
        self.types = ["loop"]
        self.entity_state = None               # This class variable is assigned by the entity’s insert_action call 
        self.name = "move_player"          # Names are frequently useful 
        self.verbose = False                   # verbose flags are handy 
        self.direction = direction
        self.key = key
        self.children = []                     # List of child actions that this action may choose to call 
 
    def condition_to_act(self, data):          # Check whether conditions are right for running this action 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False  
        if pygame.key.get_pressed()[self.key]:
            return True
        return False 
 
    def act(self, data):                       # Run this action if the conditions are right 
        if self.condition_to_act(data):        # Check whether the conditions are right 
            # print(data.key)
            # while()
            for i in range(0, len(self.entity_state.acceleration)):
                if self.entity_state.active_particle[i]:
                    self.entity_state.velocity[i][0] += self.direction[0]
                    self.entity_state.velocity[i][1] += self.direction[1]
            for c in self.children:            # Have the children act as well 
                c.act(data) 
            if self.verbose:                   # A diagnostic when the verbose is True 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return

class updateMessage(): #action
	
	def __init__(self, timer):
		self.types = ["loop"]
		self.timer = timer
		self.entity_state = None
		self.name = "generateMessage"
		self.children = []
		self.verbose = True
		
		self.timehud =  ui.make_hud( WIDTH/2,HEIGHT/2 - 100 ,"Time Spend: 123", (255, 255, 255), (0, 0, 0), size =32)
		drawTimeHudAction = ui.make_hud_action()
		self.timehud.insert_action(drawTimeHudAction)
		
	def condition_to_act(self, data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		return True
				
	def act(self,data):
		print("current time: " + str(self.timer.current_time))
		print("self.timehud: " + str(self.timehud))
		self.timehud.message = "Time Spend: s" + str(round((self.timer.current_time)/1000,2)) + " s"

class loadNewLevel():
	
	def __init__(self):
		self.types = ["level"]
		self.entity_state = None
		self.verbose = False
		self.name = "loadNewLevel"
		self.children = []
		self.content = []
		self.level = 1
		self.result = False
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
		self.loadObjects(self.level,self.result)

		if self.entity_state.entity != None:
			for c in self.entity_state.entity:
				self.entity_state.gameloop.insert_entity(c)			
		if self.verbose:
			print(self.name + " for " + self.entity_state.name)
		
		return
	
	#Not an actual action-- just a helper function
	def spawnEnemy(self, loc, direction, bound1, bound2, ppart, pwidth):
		enemy = act.make_rectangle((loc[0], loc[1], 30, 30), (255,0,0))
		drawEnemyAction = act.make_draw_rect_action()
		enemyAIAction = EnemyAI(direction, bound1, bound2)
		insideEnemyAction = act.make_is_inside_action(pwidth)
		insideEnemyAction.types.append("loop")
		insideEnemyAction.to_check.append(ppart)
		enemy.insert_action(drawEnemyAction)
		enemy.insert_action(enemyAIAction)
		enemy.insert_action(insideEnemyAction)
		return enemy, drawEnemyAction
	
	def loadObjects(self,level,mid):
		
		# clear
		self.entity_state.display.clear(True)	
		self.entity_state.entity = []
		self.entity_state.display.children = []
				
		# hud to show time result
		updateMessageAction = updateMessage(self.entity_state.timer)
		drawTimeHudAction = ui.make_hud_action()
		updateMessageAction.timehud.insert_action(drawTimeHudAction)	
		
		# hud to show level
		levelText = ui.make_hud( 100, 50 ,"level", (255, 255, 255) , (0, 0, 0), size =28)
		drawLevelHudAction = ui.make_hud_action()
		levelText.insert_action(drawLevelHudAction)	
		
		# init timer and actions
		updateTimerAction = util.make_update_timer_action()
		self.entity_state.timer.insert_action(updateTimerAction)
		startAction = util.make_start_timer_action()
		self.entity_state.timer.insert_action(startAction)

		clear = pl.make_clear_action()
		self.entity_state.gameloop.insert_action(clear)
		
		print(">>>>" + str(level))
		if(self.result == False):
			self.result = True
			self.entity_state.level = self.entity_state.level + 1
			if level==1:
				print("level" + str(level))
					
				levelText.message = "level " + str(level)
				self.entity_state.display.children.append(drawLevelHudAction) 
				self.entity_state.entity.append(levelText)					
				
				#
				# game content
				#
				#Physics-related things
				playerParticle = phys.make_particles()
				# player = act.make_rectangle((50, 50, playerWidth, playerWidth), (255,255,255))
				player = act.make_circle(playerWidth, (50, 50), (255,255,255))
				drawPlayerAction = act.make_draw_round_action()
				player.insert_action(drawPlayerAction)
				self.entity_state.display.children.append(drawPlayerAction)
				playerParticle.add_particle([50,50], [.1,.1], 1)
				playerParticle.insert_action(MovePlayer([playerSpeed,0.0], pygame.K_RIGHT))
				playerParticle.insert_action(MovePlayer([-playerSpeed,0.0], pygame.K_LEFT))
				playerParticle.insert_action(MovePlayer([0.0,-playerSpeed], pygame.K_UP))
				playerParticle.insert_action(MovePlayer([0.0,playerSpeed], pygame.K_DOWN))
				
				#Natural drag force
				drag = phys.make_drag_force()
				drag.drag_constant = 1
				dragAction = phys.make_drag_force_action()
				drag.insert_action(dragAction)
				
				#Solvers
				psolveAction = phys.make_position_solve_action()
				vsolveAction = phys.make_velocity_solve_action()
				# vsolveAction.children.append(gravityAction)
				# vsolveAction.children.append(springAction)
				vsolveAction.children.append(dragAction)
				# vsolveAction.children.append(negDragAction)
				playerParticle.insert_action(psolveAction)
				playerParticle.insert_action(vsolveAction)

				esolveAction = phys.make_euler_solve_action()
				esolveAction.dt = 0.1
				esolveAction.children.append(psolveAction)
				esolveAction.children.append(vsolveAction)
				esolveAction.types.append("loop")
				playerParticle.insert_action(esolveAction)
				
				#Go through every circle (particle) and apply the pick and put actions accordingly
				pickAction = phys.make_pick_position_action(0)
				putAction = act.make_put_position_action()
				playerParticle.insert_action(pickAction)
				player.insert_action(putAction)
				pickAction.children.append(putAction)
				esolveAction.children.append(pickAction)
				
				#Bound particles within the window 
				windowContainerCollider = phys.make_rectangle_collider([playerWidth, playerWidth], [WIDTH-playerWidth, HEIGHT-playerWidth])
				insideAction = phys.make_inside_rectangle_collider_action()
				windowContainerCollider.insert_action(insideAction)
				psolveAction.children.append(insideAction)
				
				#Make all the rectangle actors necessary for the game
				#Rect 2 is special because it is where the hole is, so it has to start inactive
				rect1 = act.make_rectangle((800, 0, 100, 200), (255,255,255))
				drawRectAction1 = act.make_draw_rect_action()
				rect1.insert_action(drawRectAction1)
				self.entity_state.display.children.append(drawRectAction1)
				rect1collider = phys.make_rectangle_collider([800-playerWidth, -10-playerWidth], [900+playerWidth, 200+playerWidth])        #I extend the reach of some of the ends of colliders to prevent particles phasing through
				isOutsideAction1 = phys.make_outside_rectangle_collider_action()
				rect1collider.insert_action(isOutsideAction1)
				psolveAction.children.append(isOutsideAction1)

				enemy1, drawE1 = self.spawnEnemy([250,250], [1,0], [150,250], [350,250], playerParticle, playerWidth)
				self.entity_state.display.children.append(drawE1)
				enemies.append(enemy1)
				byLevel.append(len(enemies)-1)

				enemy2, drawE2 = self.spawnEnemy([250,250], [0,1], [250,150], [250,350], playerParticle, playerWidth)
				self.entity_state.display.children.append(drawE2)
				enemies.append(enemy2)
				byLevel.append(len(enemies)-1)

				enemy3, drawE3 = self.spawnEnemy([250,250], [0,0], [250,150], [250,350], playerParticle, playerWidth)
				self.entity_state.display.children.append(drawE3)
				enemies.append(enemy3)
				byLevel.append(len(enemies)-1)

				enemy4, drawE4 = self.spawnEnemy([250,250], [1,1], [150,150], [350,350], playerParticle, playerWidth)
				self.entity_state.display.children.append(drawE4)
				enemies.append(enemy4)
				byLevel.append(len(enemies)-1)
				
				self.entity_state.entity.append(player)
				self.entity_state.entity.append(playerParticle)
				for e in enemies:
				    self.entity_state.entity.append(e)

				
				### End
		
				button_object = ui.make_button( (WIDTH/4*3, HEIGHT/4*3, 200, 100) , (255, 0, 0) , "button" )
				button_object.message = "press" 
				button_object.name = "press_button level 1"
				drawButtonAction = ui.make_draw_button_action()
				button_object.insert_action(drawButtonAction)
				self.entity_state.display.children.append(drawButtonAction) 
				
				self.entity_state.entity.append(button_object)	
					
				pressButtonAction = ui.make_press_button_action()
				button_object.insert_action(pressButtonAction)	
				pressButtonAction.children.append(updateMessageAction)
				pressButtonAction.children.append(clear)
				pressButtonAction.children.append(self.entity_state.actions[0])
			
			elif level==2:
				print("level" + str(level))
					
				levelText.message = "level " + str(level)
				self.entity_state.display.children.append(drawLevelHudAction) 	
				self.entity_state.entity.append(levelText)	
					
				button_object = ui.make_button( (WIDTH/4*3, HEIGHT/4*3, 200, 100) , (255, 0, 0) , "button" )
				button_object.message = "press 2" 
				button_object.name = "press_button"
				drawButtonAction = ui.make_draw_button_action()
				button_object.insert_action(drawButtonAction)
				self.entity_state.display.children.append(drawButtonAction) 

				self.entity_state.entity.append(button_object)	
					
				pressButtonAction = ui.make_press_button_action()
				button_object.insert_action(pressButtonAction)	
				pressButtonAction.children.append(updateMessageAction)
				pressButtonAction.children.append(clear)
				pressButtonAction.children.append(self.entity_state.actions[0])
		
			elif level==3:
				print("Credit" + str(level))
					
				Credit = ui.make_hud( WIDTH/2,HEIGHT/2 - 100 ,"Credit: ", (255, 255, 255), (0, 0, 0), size =40)
				drawCreditHudAction = ui.make_hud_action()
				Credit.insert_action(drawCreditHudAction)
				self.entity_state.display.children.append(drawCreditHudAction)
				Credit.active = True
				
				self.entity_state.entity.append(Credit)	
		else:
			self.result = False
			print("level 0") # show time spent
					
			self.level = self.level + 1	
			
			print("outside hud = " + str(updateMessageAction.timehud))		
			self.entity_state.entity.append(self.entity_state.timer)		
			self.entity_state.display.children.append(drawTimeHudAction)
			self.entity_state.entity.append(updateMessageAction.timehud)	
			 
			# go next button
			button_object = ui.make_button( (WIDTH/2-100, HEIGHT/2+200, 200, 100) , (255, 0, 0), "button" )
			button_object.message = "next" 
			button_object.name = "press_button 2"
			drawButtonAction = ui.make_draw_button_action()
			button_object.insert_action(drawButtonAction)
			self.entity_state.display.children.append(drawButtonAction) 
					
			pressButtonAction = ui.make_press_button_action()
			button_object.insert_action(pressButtonAction)

			pressButtonAction.children.append(startAction)
			pressButtonAction.children.append(clear)
			pressButtonAction.children.append(self.entity_state.actions[0])

			self.entity_state.entity.append(button_object)	
	

