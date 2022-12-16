import goat
import cowmoo.engine.utility as util
import cowmoo.engine.ui as ui

hud = ui.make_hud( 80,50 ,"level 8", (0, 0, 0), (200, 200, 200), size = 28)
drawHudAction = ui.make_hud_action()
hud.insert_action(drawHudAction)	


timer = util.make_timer()
startTimerAction = util.make_start_timer_action()
updateTimerAction = util.make_update_timer_action()
timer.insert_action(startTimerAction)
timer.insert_action(updateTimerAction)
player, playerParticle, drawPlayerAction, psolveAction = goat.playerSetup(goat.playerWidth, 2.5, 200, 200)
goal, drawGoalAction = goat.createGoal((200,500,60,60), "level9", playerParticle, gloop, dplay)

wall1, drawWallAction1 = goat.createWall((0,0,goat.WIDTH,100), psolveAction, goat.playerWidth)
wall2, drawWallAction2 = goat.createWall((0,100,100,goat.HEIGHT-200), psolveAction, goat.playerWidth)
wall3, drawWallAction3 = goat.createWall((goat.WIDTH-100,100,100,goat.HEIGHT-200), psolveAction, goat.playerWidth)
wall4, drawWallAction4 = goat.createWall((0,goat.HEIGHT-100,goat.WIDTH,100), psolveAction, goat.playerWidth)

wall5, drawWallAction5 = goat.createWall((0,goat.HEIGHT/2-50,goat.WIDTH/3*2,100), psolveAction, goat.playerWidth)

enemy, drawEnemyAction = goat.spawnEnemy([300,100], [0,1], [300,100], [300,goat.HEIGHT/2-80], playerParticle, goat.playerWidth, "level8", gloop, dplay)
enemy2, drawEnemyAction2 = goat.spawnEnemy([600,150], [0,1], [600,100], [600,goat.HEIGHT/2-80], playerParticle, goat.playerWidth, "level8", gloop, dplay)
enemy3, drawEnemyAction3 = goat.spawnEnemy([400,goat.HEIGHT/2+50], [0,1], [400,goat.HEIGHT/2+50], [400,goat.HEIGHT-130], playerParticle, goat.playerWidth, "level8", gloop, dplay)
enemy4, drawEnemyAction4 = goat.spawnEnemy([800,goat.HEIGHT/2+80], [0,1], [800,goat.HEIGHT/2+50], [800,goat.HEIGHT-130], playerParticle, goat.playerWidth, "level8", gloop, dplay)

entity_list = [wall1, wall2, wall3, wall4, wall5, enemy, enemy2, enemy3, enemy4]
display_list = [drawWallAction1, drawWallAction2, drawWallAction3, drawWallAction4,
				drawWallAction5, drawEnemyAction, drawEnemyAction2, drawEnemyAction3, drawEnemyAction4]

entities.append(player)
entities.append(playerParticle)
entities.append(goal)
entities.append(timer)
entities.append(hud)
displayActions.append(drawPlayerAction)
displayActions.append(drawGoalAction)

for e in entity_list:
	entities.append(e)
for a in display_list:
	displayActions.append(a)
	
displayActions.append(drawHudAction)
	
entity_list.clear()
display_list.clear()
