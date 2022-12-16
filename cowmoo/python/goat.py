import sys
sys.path.append("../..")
import cowmoo.engine.play as pl 
import cowmoo.engine.ui as ui 
import cowmoo.engine.utility as util 
import cowmoo.engine.physics as phys
import cowmoo.engine.actor as act
import cowmoo.engine.sound as snd
import pygame 
import random
import copy

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
    
class CounterEqualTo:
    def __init__(self, val):
        self.types = ["loop"]
        self.entity_state = None               # This class variable is assigned by the entity’s insert_action call 
        self.name = "counter_equal_to"          # Names are frequently useful 
        self.verbose = False                   # verbose flags are handy 
        self.val = val
        self.children = []                     # List of child actions that this action may choose to call 
 
    def condition_to_act(self, data):          # Check whether conditions are right for running this action 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False  
        if self.entity_state.counter_value == self.val:
            return True
        return False 
 
    def act(self, data):                       # Run this action if the conditions are right 
        if self.condition_to_act(data):        # Check whether the conditions are right 
            for c in self.children:            # Have the children act as well 
                c.act(data) 
            if self.verbose:                   # A diagnostic when the verbose is True 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return
    
class PrintTimerMessage:
    def __init__(self, lvlname):
        self.types = []
        self.entity_state = None               # This class variable is assigned by the entity’s insert_action call 
        self.name = "print_timer_message"          # Names are frequently useful 
        self.verbose = False                   # verbose flags are handy 
        self.lvlname = lvlname
        self.children = []                     # List of child actions that this action may choose to call 
 
    def condition_to_act(self, data):          # Check whether conditions are right for running this action 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False  
        return True 
 
    def act(self, data):                       # Run this action if the conditions are right 
        if self.condition_to_act(data):        # Check whether the conditions are right 
            print("Time taken for", self.lvlname, "-", self.entity_state.elapsed_time()/1000)
            for c in self.children:            # Have the children act as well 
                c.act(data) 
            if self.verbose:                   # A diagnostic when the verbose is True 
                print( self.name + " for " + self.entity_state.name + " at " + str(event.pos)) 
        return     

def playerSetup(playerWidth=20, playerSpeed=2.5, positionX = 50, positionY = 50, WIDTH=1280, HEIGHT=720):
    #Physics-related things
    playerParticle = phys.make_particles()
    # player = act.make_rectangle((50, 50, playerWidth, playerWidth), (255,255,255))
    player = act.make_circle(playerWidth, (positionX, positionY), (255,255,255))
    drawPlayerAction = act.make_draw_round_action()
    player.insert_action(drawPlayerAction)
    # display.children.append(drawPlayerAction)
    playerParticle.add_particle([positionX,positionY], [.1,.1], 1)
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
    vsolveAction.children.append(dragAction)
    playerParticle.insert_action(psolveAction)
    playerParticle.insert_action(vsolveAction)

    esolveAction = phys.make_euler_solve_action()
    esolveAction.dt = 0.1
    esolveAction.children.append(psolveAction)
    esolveAction.children.append(vsolveAction)
    esolveAction.types.append("loop")
    playerParticle.insert_action(esolveAction)

    pickAction = phys.make_pick_position_action(0)
    putAction = act.make_put_position_action()
    playerParticle.insert_action(pickAction)
    player.insert_action(putAction)
    pickAction.children.append(putAction)
    esolveAction.children.append(pickAction)

    windowContainerCollider = phys.make_rectangle_collider([playerWidth, playerWidth], [WIDTH-playerWidth, HEIGHT-playerWidth])
    insideAction = phys.make_inside_rectangle_collider_action()
    windowContainerCollider.insert_action(insideAction)
    psolveAction.children.append(insideAction)
    return player, playerParticle, drawPlayerAction, psolveAction

def createGoal(bounds, nextLevelName, ppart, gloop, dplay, timer, playerWidth=20):
    goal = act.make_rectangle(bounds, (0,255,0))
    goalDrawAction = act.make_draw_rect_action()
    insideGoalAction = act.make_is_inside_action(playerWidth)
    insideGoalAction.to_check.append(ppart)
    insideGoalAction.types.append("loop")
    loadNewLvlAction = pl.make_load_lvl_action(nextLevelName, gloop, dplay)
    printMessageAction = PrintTimerMessage(nextLevelName[0:5] + str(int(nextLevelName[5:])-1))
    timer.insert_action(printMessageAction)
    soundAction = snd.make_emit_sound_action("goal.wav")
    soundAction.set_volume(.5)
    insideGoalAction.children.append(soundAction)
    insideGoalAction.children.append(printMessageAction)
    insideGoalAction.children.append(loadNewLvlAction)
    goal.insert_action(goalDrawAction)
    goal.insert_action(insideGoalAction)
    goal.insert_action(soundAction)
    return goal, goalDrawAction

def spawnEnemy(loc, direction, bound1, bound2, ppart, pwidth, currLevel, gloop, dplay):
    enemy = act.make_rectangle((loc[0], loc[1], 30, 30), (255,0,0))
    drawEnemyAction = act.make_draw_rect_action()
    enemyAIAction = EnemyAI(direction, bound1, bound2)
    insideEnemyAction = act.make_is_inside_action(pwidth)
    insideEnemyAction.types.append("loop")
    insideEnemyAction.to_check.append(ppart)
    reloadLvlAction = pl.make_load_lvl_action(currLevel, gloop, dplay)
    insideEnemyAction.children.append(reloadLvlAction)
    soundAction = snd.make_emit_sound_action("hitHurt.wav")
    soundAction.set_volume(.5)
    insideEnemyAction.children.append(soundAction)
    enemy.insert_action(drawEnemyAction)
    enemy.insert_action(enemyAIAction)
    enemy.insert_action(insideEnemyAction)
    enemy.insert_action(soundAction)
    return enemy, drawEnemyAction

def createWall(bounds, psolveAction, playerWidth=20, coinsToUnlock=0, counter=None):
    rect1 = act.make_rectangle(bounds, (200,200,200))
    drawRectAction1 = act.make_draw_rect_action()
    rect1.insert_action(drawRectAction1)
    rect1collider = phys.make_rectangle_collider([bounds[0]-playerWidth, bounds[1]-playerWidth], [bounds[0]+bounds[2]+playerWidth, bounds[1]+bounds[3]+playerWidth])        #I extend the reach of some of the ends of colliders to prevent particles phasing through
    isOutsideAction1 = phys.make_outside_rectangle_collider_action()
    rect1collider.insert_action(isOutsideAction1)
    psolveAction.children.append(isOutsideAction1)
    if coinsToUnlock > 0:
        rect1.color = (237, 176, 7)
        deactivateAction1 = util.make_deactivate_entity_action()
        deactivateAction2 = util.make_deactivate_entity_action()
        rect1.insert_action(deactivateAction1)
        rect1collider.insert_action(deactivateAction2)
        equalToAction = CounterEqualTo(coinsToUnlock)
        equalToAction.children.append(deactivateAction1)
        equalToAction.children.append(deactivateAction2)
        counter.insert_action(equalToAction)
    return rect1, drawRectAction1
    
def createCoin(loc, ppart, pwidth, countAction):
    coin = act.make_rectangle((loc[0], loc[1], 20, 20), (246,255,0))
    drawCoinAction = act.make_draw_rect_action()
    insideCoinAction = act.make_is_inside_action(pwidth)
    insideCoinAction.types.append("loop")
    insideCoinAction.to_check.append(ppart)
    deactivateAction = util.make_deactivate_entity_action()
    soundAction = snd.make_emit_sound_action("pickupCoin.wav")
    soundAction.set_volume(.5)
    insideCoinAction.children.append(soundAction)
    insideCoinAction.children.append(countAction)
    insideCoinAction.children.append(deactivateAction)
    coin.insert_action(drawCoinAction)
    coin.insert_action(insideCoinAction)
    coin.insert_action(deactivateAction)
    coin.insert_action(soundAction)
    return coin, drawCoinAction    

    
WIDTH = 1280
HEIGHT = 720
playerWidth = 20

if __name__ == "__main__":
    #Declare some constants
    
    playerWidth = 20
    playerSpeed = 2.5
    enemies = []

    #Non-physics entities
    game_looper = pl.make_game_loop() 
    game_looper.verbose = False 
    viewer = pl.make_frame_viewer(WIDTH,HEIGHT) 
    viewer.set_title("World's Most Not Easiest Game")
    viewer.insert_action(  pl.make_terminate_action() )
    display = pl.make_update_display_action() 
    viewer.insert_action(display)
    timer = util.make_timer()

    # start button
    start_button = ui.make_button( (WIDTH/2-100, HEIGHT/2-50, 200, 100) , (255, 255, 255), "start_button" )
    start_button.message = "start"

    drawButtonAction = ui.make_draw_button_action()
    start_button.insert_action(drawButtonAction)	
    display.children.append(drawButtonAction)
    startLevel1 = pl.make_load_lvl_action("level1", game_looper, display)
    # Loader.display.children.append(drawButtonAction)

    musicAction = snd.make_emit_sound_action("bgm.wav", -1)
    musicAction.set_volume(.2)

    pressButtonAction = ui.make_press_button_action()
    pressButtonAction.children.append(musicAction)
    pressButtonAction.children.append(startLevel1)
    start_button.insert_action(pressButtonAction)	
    start_button.insert_action(musicAction)
    # pressButtonAction.children.append(clear)
    # pressButtonAction.children.append(startAction)
    # pressButtonAction.children.append(LoadAction)
    
    

    ### Switch here ####
    #viewer.insert_action(display)
    # viewer.insert_action(Loader.display)

    #Insert entities into the game looper
    game_looper.insert_entity(viewer)
    # game_looper.insert_entity(player)
    # game_looper.insert_entity(playerParticle)
    # game_looper.insert_entity(timer)
    game_looper.insert_entity(start_button)
    # for e in enemies:
    #     game_looper.insert_entity(e)

    # for en in Loader.entity:
    #     game_looper.insert_entity(en)

    # Loader.gameloop = game_looper

    #Finally, loop
    game_looper.loop()
