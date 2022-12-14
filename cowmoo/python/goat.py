import sys
sys.path.append("../..")
import cowmoo.engine.play as pl 
import cowmoo.engine.ui as ui 
import cowmoo.engine.utility as util 
import cowmoo.engine.physics as phys
import cowmoo.engine.actor as act
import pygame 
import random

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

#Declare some constants
WIDTH = 1280
HEIGHT = 720
playerWidth = 20
playerSpeed = 2.5


#Non-physics entities
game_looper = pl.make_game_loop() 
game_looper.verbose = False 
viewer = pl.make_frame_viewer(WIDTH,HEIGHT) 
viewer.set_title("The Worlds")
viewer.insert_action(  pl.make_terminate_action() )
display = pl.make_update_display_action() 
button = ui.make_button((0,0,WIDTH,HEIGHT), (0,0,0), "screenButton")
timer = util.make_timer()

#Physics-related things
playerParticle = phys.make_particles()
# player = act.make_rectangle((50, 50, playerWidth, playerWidth), (255,255,255))
player = act.make_circle(playerWidth, (50, 50), (255,255,255))
drawPlayerAction = act.make_draw_round_action()
player.insert_action(drawPlayerAction)
display.children.append(drawPlayerAction)
playerParticle.add_particle([50,50], [.1,.1], 1)
playerParticle.insert_action(MovePlayer([playerSpeed,0.0], pygame.K_RIGHT))
playerParticle.insert_action(MovePlayer([-playerSpeed,0.0], pygame.K_LEFT))
playerParticle.insert_action(MovePlayer([0.0,-playerSpeed], pygame.K_UP))
playerParticle.insert_action(MovePlayer([0.0,playerSpeed], pygame.K_DOWN))
# particles = phys.make_particles()
# circles = []
# for i in range(100):
#     circle = act.make_circle(particleRadius, (random.randint(200, 400), random.randint(50, 250)),       #Spawn circles in a box on the topleft side of the screen
#              (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
#     drawCircleAction = act.make_draw_round_action()
#     circle.insert_action(drawCircleAction)
#     circles.append(circle)
#     display.children.append(drawCircleAction)
#     particles.add_particle([circle.center[0], circle.center[1]], [30.0, 0], 1.0)        #Starting velocity of 30 to the right

#Natural gravity force
# gravity = phys.make_gravity_force()
# gravity.gravity = [0.0, .2]
# gravityAction = phys.make_gravity_force_action()
# gravity.insert_action(gravityAction)

#Natural spring force
# spring = phys.make_spring_force()
# spring.spring_constant = .01
# springAction = phys.make_spring_force_action()
# spring.insert_action(springAction)

#Natural drag force
drag = phys.make_drag_force()
drag.drag_constant = 1
dragAction = phys.make_drag_force_action()
drag.insert_action(dragAction)

#User-initiated drag forced
# negDrag = phys.make_drag_force()
# negDrag.active = False
# negDrag.drag_constant = -1.0
# negDragAction = phys.make_drag_force_action()
# negDrag.insert_action(negDragAction)
# turnNegDragOn = util.make_activate_entity_action()
# turnNegDragOff = util.make_deactivate_entity_action()
# negDrag.insert_action(turnNegDragOn)
# negDrag.insert_action(turnNegDragOff)

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

#For turning on and off certain forces
# activateSpringAction = phys.make_activate_physics_action(["spring"])
# activateDragAction = phys.make_activate_physics_action(["drag"])
# deactivateDragAction = phys.make_deactivate_physics_action(["drag"])
# deactivateSpringAction = phys.make_deactivate_physics_action(["spring"])
# particles.insert_action(activateSpringAction)
# particles.insert_action(activateDragAction)
# particles.insert_action(deactivateDragAction)
# particles.insert_action(deactivateSpringAction)

#Go through every circle (particle) and apply the pick and put actions accordingly
pickAction = phys.make_pick_position_action(0)
putAction = act.make_put_position_action()
playerParticle.insert_action(pickAction)
player.insert_action(putAction)
pickAction.children.append(putAction)
esolveAction.children.append(pickAction)
# for i in range(len(circles)):
#     pickAction = phys.make_pick_position_action(i)
#     putAction = act.make_put_position_action()

#     particles.insert_action(pickAction)
#     circles[i].insert_action(putAction)
#     pickAction.children.append(putAction)
#     esolveAction.children.append(pickAction)

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
display.children.append(drawRectAction1)
rect1collider = phys.make_rectangle_collider([800-playerWidth, -10-playerWidth], [900+playerWidth, 200+playerWidth])        #I extend the reach of some of the ends of colliders to prevent particles phasing through
isOutsideAction1 = phys.make_outside_rectangle_collider_action()
rect1collider.insert_action(isOutsideAction1)
psolveAction.children.append(isOutsideAction1)

#Make the rectangles for checking which side of the screen the particles are on
# leftRect = act.make_rectangle((0, 0, 850, HEIGHT), (255,255,255))
# isInsideActionLeft = act.make_is_inside_action()
# isInsideActionLeft.types.append("loop")
# isInsideActionLeft.to_check.append(particles)
# isInsideActionLeft.children.append(activateSpringAction)
# isInsideActionLeft.children.append(deactivateDragAction)
# leftRect.insert_action(isInsideActionLeft)


#Actions and children of non-physics objects I hadn't dealt with yet (I know it's kind of unorganized but I wanted to deal with all physics objects at the same time)
#Plus none of this is stuff I didn't do last project, anyways, so this is mostly reused code
updateTimerAction = util.make_update_timer_action()
alarmAction = util.make_alarm_action(9000)
startAction = util.make_start_timer_action()
# alarmAction.children.append(activateRect2Action)
# alarmAction.children.append(activateRect2ColliderAction)
updateTimerAction.children.append(alarmAction)
timer.insert_action(updateTimerAction)
timer.insert_action(startAction)
timer.insert_action(alarmAction)
pressAction = ui.make_press_button_action()
button.insert_action(pressAction)
viewer.insert_action(display)

#Insert entities into the game looper
game_looper.insert_entity(viewer)
game_looper.insert_entity(button)
game_looper.insert_entity(player)
game_looper.insert_entity(playerParticle)
game_looper.insert_entity(timer)

#Finally, loop
game_looper.loop()