import goat
import cowmoo.engine.utility as util
import cowmoo.engine.ui as ui

hud = ui.make_hud( 80,50 ,"level 10", (0, 0, 0), (200, 200, 200), size = 28)
drawHudAction = ui.make_hud_action()
hud.insert_action(drawHudAction)	

timer = util.make_timer()
startTimerAction = util.make_start_timer_action()
updateTimerAction = util.make_update_timer_action()
timer.insert_action(startTimerAction)
timer.insert_action(updateTimerAction)
player, playerParticle, drawPlayerAction, psolveAction = goat.playerSetup(goat.playerWidth, 2.5, 200, 200)
# print(player, playerParticle, drawPlayerAction)
goal, drawGoalAction = goat.createGoal((1000,500,60,30), "level11", playerParticle, gloop, dplay, timer)

wall1, drawWallAction1 = goat.createWall((0,0,goat.WIDTH,100), psolveAction, goat.playerWidth)
wall2, drawWallAction2 = goat.createWall((0,100,100,goat.HEIGHT-200), psolveAction, goat.playerWidth)
wall3, drawWallAction3 = goat.createWall((goat.WIDTH-100,100,100,goat.HEIGHT-200), psolveAction, goat.playerWidth)
wall4, drawWallAction4 = goat.createWall((0,goat.HEIGHT-100,goat.WIDTH,100), psolveAction, goat.playerWidth)
wall5, drawWallAction5 = goat.createWall((400,0,50,400), psolveAction, goat.playerWidth)
wall6, drawWallAction6 = goat.createWall((800,goat.HEIGHT-400,50,400), psolveAction, goat.playerWidth)

enemy, drawEnemyAction = goat.spawnEnemy([100,400], [1,0], [100,400], [400,400], playerParticle, goat.playerWidth, "level10", gloop, dplay)
enemy2, drawEnemyAction2 = goat.spawnEnemy([800,100], [0,1], [800,100], [800,300], playerParticle, goat.playerWidth, "level10", gloop, dplay)
enemy3, drawEnemyAction3 = goat.spawnEnemy([450,100], [1,1], [450,100], [770,450], playerParticle, goat.playerWidth, "level10", gloop, dplay)
enemy4, drawEnemyAction4 = goat.spawnEnemy([600,100], [0,1], [600,100], [600,goat.HEIGHT-130], playerParticle, goat.playerWidth, "level10", gloop, dplay)
enemy5, drawEnemyAction5 = goat.spawnEnemy([450,500], [1,0], [100,500], [770,500], playerParticle, goat.playerWidth, "level10", gloop, dplay)
enemy6, drawEnemyAction6 = goat.spawnEnemy([900,400], [1,0], [850,400], [goat.WIDTH-130,400], playerParticle, goat.playerWidth, "level10", gloop, dplay)

entity_list = [wall1, wall2, wall3, wall4, wall5, wall6, enemy, enemy2, enemy3, enemy4, enemy5, enemy6]
display_list = [drawWallAction1, drawWallAction2, drawWallAction3, drawWallAction4, 
				drawWallAction5, drawWallAction6, drawEnemyAction, drawEnemyAction2,
				drawEnemyAction3, drawEnemyAction4, drawEnemyAction5, drawEnemyAction6]

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
