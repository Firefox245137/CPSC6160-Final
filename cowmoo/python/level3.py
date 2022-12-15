import goat
import cowmoo.engine.utility as util

timer = util.make_timer()
startTimerAction = util.make_start_timer_action()
updateTimerAction = util.make_update_timer_action()
timer.insert_action(startTimerAction)
timer.insert_action(updateTimerAction)
player, playerParticle, drawPlayerAction, psolveAction = goat.playerSetup(goat.playerWidth, 2.5)
goal, drawGoalAction = goat.createGoal((1050,520,60,60), "level3", playerParticle, gloop, dplay)

wall1, drawWallAction1 = goat.createWall((0,0,goat.WIDTH,100), psolveAction, goat.playerWidth)
wall2, drawWallAction2 = goat.createWall((0,100,100,goat.HEIGHT-200), psolveAction, goat.playerWidth)
wall3, drawWallAction3 = goat.createWall((goat.WIDTH-100,100,100,goat.HEIGHT-200), psolveAction, goat.playerWidth)
wall4, drawWallAction4 = goat.createWall((0,goat.HEIGHT-100,goat.WIDTH,100), psolveAction, goat.playerWidth)

wall5, drawWallAction5 = goat.createWall((100,250,900,50), psolveAction, goat.playerWidth)
wall6, drawWallAction6 = goat.createWall((goat.WIDTH-1000,goat.HEIGHT-280,900,50), psolveAction, goat.playerWidth)

wall7, drawWallAction7 = goat.createWall((300,300,50,70), psolveAction, goat.playerWidth)
wall8, drawWallAction8 = goat.createWall((600,goat.HEIGHT-350,50,70), psolveAction, goat.playerWidth)
wall9, drawWallAction9 = goat.createWall((900,300,50,70), psolveAction, goat.playerWidth)

entity_list = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9]
display_list = [drawWallAction1, drawWallAction2, drawWallAction3, drawWallAction4, drawWallAction5, drawWallAction6, drawWallAction7,
				drawWallAction8, drawWallAction9]

entities.append(player)
entities.append(playerParticle)
entities.append(goal)
entities.append(timer)
displayActions.append(drawPlayerAction)
displayActions.append(drawGoalAction)

for e in entity_list:
	entities.append(e)
for a in display_list:
	displayActions.append(a)
	
entity_list.clear()
display_list.clear()
