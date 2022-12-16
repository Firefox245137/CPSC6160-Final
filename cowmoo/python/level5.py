import goat
import cowmoo.engine.utility as util
import cowmoo.engine.ui as ui

hud = ui.make_hud( 80,50 ,"level 5", (0, 0, 0), (200, 200, 200), size = 28)
drawHudAction = ui.make_hud_action()
hud.insert_action(drawHudAction)	

timer = util.make_timer()
startTimerAction = util.make_start_timer_action()
updateTimerAction = util.make_update_timer_action()
timer.insert_action(startTimerAction)
timer.insert_action(updateTimerAction)
# print(timer, type(timer), updateTimerAction.__class__.__name__ == "UpdateTimer")
player, playerParticle, drawPlayerAction, psolveAction = goat.playerSetup(goat.playerWidth, 2.5, 500, 360)
# print(player, playerParticle, drawPlayerAction)
goal, drawGoalAction = goat.createGoal((goat.WIDTH-260,200,60,goat.HEIGHT-400), "level6", playerParticle, gloop, dplay, timer)

wall1, drawWallAction1 = goat.createWall((0,0,goat.WIDTH,200), psolveAction, goat.playerWidth)
wall2, drawWallAction2 = goat.createWall((0,200,200,goat.HEIGHT-400), psolveAction, goat.playerWidth)
wall3, drawWallAction3 = goat.createWall((goat.WIDTH-200,200,200,goat.HEIGHT-400), psolveAction, goat.playerWidth)
wall4, drawWallAction4 = goat.createWall((0,goat.HEIGHT-200,goat.WIDTH,200), psolveAction, goat.playerWidth)

enemy, drawEnemyAction = goat.spawnEnemy([700,250], [0,1], [700,200], [700,490], playerParticle, goat.playerWidth, "level5", gloop, dplay)


entity_list = [wall1, wall2, wall3, wall4, enemy]
display_list = [drawWallAction1, drawWallAction2, drawWallAction3, drawWallAction4, drawEnemyAction]

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
	
displayActions.append(drawHudAction)
	
entity_list.clear()
display_list.clear()


