### This is a "level" file: it's where all the actual "game" code is written
### There are 23 level files, so I am NOT commenting on all of them, BUT since the "level" files are all functionally the 
### same, just with different placement of entites, I am going to comment on this file, and it will apply to just about all the other files

## Since the load level function is built off of exec(), variables from the load_level.py function exist in this function
## Because I want to avoid confusion, I will list the passed down variables
##      gloop - The Game Looper entity
##      dplay - The UpdateDisplay Action
##      entities - An empty list ([]) which will be added to in this file       (for entities)
##      displayActions - An empty list([]) which will be added to in this file  (for display actions, specifically)

#First, we need to import the 'main' level, in this case it is goat.py (and also we import anything we need from our game engine)
import goat
import cowmoo.engine.utility as util
import cowmoo.engine.ui as ui

#Text to display level name
hud = ui.make_hud( 80,50 ,"level 1", (0, 0, 0), (200, 200, 200), size = 28)
drawHudAction = ui.make_hud_action()
hud.insert_action(drawHudAction)	

#[6160 requirement] Create a timer entity 
timer = util.make_timer()
startTimerAction = util.make_start_timer_action()
updateTimerAction = util.make_update_timer_action()
timer.insert_action(startTimerAction)
timer.insert_action(updateTimerAction)

#Spawn in the player and the goal - all aspects are controllable, e.g. you can have player with width 500 who spawns at 0,0
player, playerParticle, drawPlayerAction, psolveAction = goat.playerSetup(goat.playerWidth, 2.5, 500, 360)
goal, drawGoalAction = goat.createGoal((goat.WIDTH-260,200,60,goat.HEIGHT-400), "level2", playerParticle, gloop, dplay, timer)

#Spawn in walls
wall1, drawWallAction1 = goat.createWall((0,0,goat.WIDTH,200), psolveAction, goat.playerWidth)
wall2, drawWallAction2 = goat.createWall((0,200,200,goat.HEIGHT-400), psolveAction, goat.playerWidth)
wall3, drawWallAction3 = goat.createWall((goat.WIDTH-200,200,200,goat.HEIGHT-400), psolveAction, goat.playerWidth)
wall4, drawWallAction4 = goat.createWall((0,goat.HEIGHT-200,goat.WIDTH,200), psolveAction, goat.playerWidth)

#Idk exactly how exec() works, but we can't modify the entities list directly (e.g. entities = [wall1] doesn't work for some reason) so we make temp lists and then iterate through them later
entity_list = [wall1, wall2, wall3, wall4]
display_list = [drawWallAction1, drawWallAction2, drawWallAction3, drawWallAction4]

entities.append(player)
entities.append(playerParticle)
entities.append(goal)
entities.append(timer)
displayActions.append(drawPlayerAction)
displayActions.append(drawGoalAction)

#Iterate through temp lists and add them into the load_level lists
for e in entity_list:
	entities.append(e)
for a in display_list:
	displayActions.append(a)
	
displayActions.append(drawHudAction)
	
entity_list.clear()
display_list.clear()


### After comment: the first level is relatively simple, i.e. there's no enemies, coins, or coinwalls, but all of those things are spawned in the same way the wall is
### Also, coins need a Counter Entity from the game engine, but those are simply created in the way the Timer is here