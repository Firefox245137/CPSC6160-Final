import sys
sys.path.append("../..")
import cowmoo.engine.play as pl 
import cowmoo.engine.ui as ui 
import cowmoo.engine.utility as util 
import cowmoo.engine.physics as phys
import cowmoo.engine.actor as act
import pygame 
import random
 
#Declare some constants
WIDTH = 1280
HEIGHT = 720
particleRadius = 10


#Non-physics entities
game_looper = pl.make_game_loop() 
game_looper.verbose = False 
viewer = pl.make_frame_viewer(WIDTH,HEIGHT) 
viewer.set_title("Cannon Fodder")
viewer.insert_action(  pl.make_terminate_action() )
display = pl.make_update_display_action() 
button = ui.make_button((0,0,WIDTH,HEIGHT), (0,0,0), "screenButton")
timer = util.make_timer()

#Physics-related things
particles = phys.make_particles()
circles = []
for i in range(100):
    circle = act.make_circle(particleRadius, (random.randint(200, 400), random.randint(50, 250)),       #Spawn circles in a box on the topleft side of the screen
             (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    drawCircleAction = act.make_draw_round_action()
    circle.insert_action(drawCircleAction)
    circles.append(circle)
    display.children.append(drawCircleAction)
    particles.add_particle([circle.center[0], circle.center[1]], [30.0, 0], 1.0)        #Starting velocity of 30 to the right

#Natural gravity force
gravity = phys.make_gravity_force()
gravity.gravity = [0.0, .2]
gravityAction = phys.make_gravity_force_action()
gravity.insert_action(gravityAction)

#Natural spring force
spring = phys.make_spring_force()
spring.spring_constant = .01
springAction = phys.make_spring_force_action()
spring.insert_action(springAction)

#Natural drag force
drag = phys.make_drag_force()
drag.drag_constant = .02
dragAction = phys.make_drag_force_action()
drag.insert_action(dragAction)

#User-initiated drag forced
negDrag = phys.make_drag_force()
negDrag.active = False
negDrag.drag_constant = -1.0
negDragAction = phys.make_drag_force_action()
negDrag.insert_action(negDragAction)
turnNegDragOn = util.make_activate_entity_action()
turnNegDragOff = util.make_deactivate_entity_action()
negDrag.insert_action(turnNegDragOn)
negDrag.insert_action(turnNegDragOff)

#Solvers
psolveAction = phys.make_position_solve_action()
vsolveAction = phys.make_velocity_solve_action()
vsolveAction.children.append(gravityAction)
vsolveAction.children.append(springAction)
vsolveAction.children.append(dragAction)
vsolveAction.children.append(negDragAction)
particles.insert_action(psolveAction)
particles.insert_action(vsolveAction)

esolveAction = phys.make_euler_solve_action()
esolveAction.dt = 0.1
esolveAction.children.append(psolveAction)
esolveAction.children.append(vsolveAction)
esolveAction.types.append("loop")
particles.insert_action(esolveAction)

#For turning on and off certain forces
activateSpringAction = phys.make_activate_physics_action(["spring"])
activateDragAction = phys.make_activate_physics_action(["drag"])
deactivateDragAction = phys.make_deactivate_physics_action(["drag"])
deactivateSpringAction = phys.make_deactivate_physics_action(["spring"])
particles.insert_action(activateSpringAction)
particles.insert_action(activateDragAction)
particles.insert_action(deactivateDragAction)
particles.insert_action(deactivateSpringAction)

#Go through every circle (particle) and apply the pick and put actions accordingly
for i in range(len(circles)):
    pickAction = phys.make_pick_position_action(i)
    putAction = act.make_put_position_action()

    particles.insert_action(pickAction)
    circles[i].insert_action(putAction)
    pickAction.children.append(putAction)
    esolveAction.children.append(pickAction)

#Bound particles within the window 
windowContainerCollider = phys.make_rectangle_collider([0.0, 0.0], [WIDTH, HEIGHT])
insideAction = phys.make_inside_rectangle_collider_action()
windowContainerCollider.insert_action(insideAction)
psolveAction.children.append(insideAction)

#Make all the rectangle actors necessary for the game
#Rect 2 is special because it is where the hole is, so it has to start inactive
rect1 = act.make_rectangle((800, 0, 100, 200), (255,255,255))
drawRectAction1 = act.make_draw_rect_action()
rect1.insert_action(drawRectAction1)
display.children.append(drawRectAction1)
rect1collider = phys.make_rectangle_collider([800, -10], [900, 200])        #I extend the reach of some of the ends of colliders to prevent particles phasing through
isOutsideAction1 = phys.make_outside_rectangle_collider_action()
rect1collider.insert_action(isOutsideAction1)
psolveAction.children.append(isOutsideAction1)

rect2 = act.make_rectangle((800, 200, 100, 50), (255,255,255))
rect2.active = False
drawRectAction2 = act.make_draw_rect_action()
activateRect2Action = util.make_activate_entity_action()
rect2.insert_action(drawRectAction2)
rect2.insert_action(activateRect2Action)
display.children.append(drawRectAction2)
rect2collider = phys.make_rectangle_collider([800, 200], [900, 250])
rect2collider.active = False
isOutsideAction2 = phys.make_outside_rectangle_collider_action()
activateRect2ColliderAction = util.make_activate_entity_action()
rect2collider.insert_action(isOutsideAction2)
rect2collider.insert_action(activateRect2ColliderAction)
psolveAction.children.append(isOutsideAction2)

rect3 = act.make_rectangle((800, 250, 100, HEIGHT-250), (255,255,255))
drawRectAction3 = act.make_draw_rect_action()
rect3.insert_action(drawRectAction3)
display.children.append(drawRectAction3)
rect3collider = phys.make_rectangle_collider([800, 250], [900, HEIGHT+10])
isOutsideAction3 = phys.make_outside_rectangle_collider_action()
rect3collider.insert_action(isOutsideAction3)
psolveAction.children.append(isOutsideAction3)

rect4 = act.make_rectangle((1000, 500, 150, 25), (255,255,255))
drawRectAction4 = act.make_draw_rect_action()
rect4.insert_action(drawRectAction4)
display.children.append(drawRectAction4)
rect4collider = phys.make_rectangle_collider([1000, 500], [1150, 525])
isOutsideAction4 = phys.make_outside_rectangle_collider_action()
rect4collider.insert_action(isOutsideAction4)
psolveAction.children.append(isOutsideAction4)

rect5 = act.make_rectangle((1050, 600, 150, 25), (255,255,255))
drawRectAction5 = act.make_draw_rect_action()
rect5.insert_action(drawRectAction5)
display.children.append(drawRectAction5)
rect5collider = phys.make_rectangle_collider([1050, 600], [1200, 625])
isOutsideAction5 = phys.make_outside_rectangle_collider_action()
rect5collider.insert_action(isOutsideAction5)
psolveAction.children.append(isOutsideAction5)

#Make the rectangles for checking which side of the screen the particles are on
leftRect = act.make_rectangle((0, 0, 850, HEIGHT), (255,255,255))
isInsideActionLeft = act.make_is_inside_action()
isInsideActionLeft.types.append("loop")
isInsideActionLeft.to_check.append(particles)
isInsideActionLeft.children.append(activateSpringAction)
isInsideActionLeft.children.append(deactivateDragAction)
leftRect.insert_action(isInsideActionLeft)

rightRect = act.make_rectangle((850, 0, WIDTH-850, HEIGHT), (255,255,255))
isInsideActionRight = act.make_is_inside_action()
isInsideActionRight.types.append("loop")
isInsideActionRight.to_check.append(particles)
isInsideActionRight.children.append(activateDragAction)
isInsideActionRight.children.append(deactivateSpringAction)
rightRect.insert_action(isInsideActionRight)

#Actions and children of non-physics objects I hadn't dealt with yet (I know it's kind of unorganized but I wanted to deal with all physics objects at the same time)
#Plus none of this is stuff I didn't do last project, anyways, so this is mostly reused code
updateTimerAction = util.make_update_timer_action()
alarmAction = util.make_alarm_action(9000)
startAction = util.make_start_timer_action()
alarmAction.children.append(activateRect2Action)
alarmAction.children.append(activateRect2ColliderAction)
updateTimerAction.children.append(alarmAction)
timer.insert_action(updateTimerAction)
timer.insert_action(startAction)
timer.insert_action(alarmAction)
pressAction = ui.make_press_button_action()
pressAction.children.append(turnNegDragOn)              #6160 component
pressAction.children.append(esolveAction)               #To the press action, I add an action to turn negative drag on, do a euler solve, and then turn negative drag back off
pressAction.children.append(turnNegDragOff)  
button.insert_action(pressAction)
viewer.insert_action(display)

#Insert entities into the game looper
game_looper.insert_entity(viewer)
game_looper.insert_entity(button)
game_looper.insert_entity(particles)
game_looper.insert_entity(timer)
for i in range(len(circles)):
    game_looper.insert_entity(circles[i])
game_looper.insert_entity(leftRect)
game_looper.insert_entity(rightRect)

#Finally, loop
game_looper.loop()