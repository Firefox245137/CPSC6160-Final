import goat
import cowmoo.engine.utility as util
import cowmoo.engine.ui as ui

hud = ui.make_hud( 80,50 ,"level 19", (0, 0, 0), (200, 200, 200), size = 28)
drawHudAction = ui.make_hud_action()
hud.insert_action(drawHudAction)	

timer = util.make_timer()
startTimerAction = util.make_start_timer_action()
updateTimerAction = util.make_update_timer_action()
timer.insert_action(startTimerAction)
timer.insert_action(updateTimerAction)
player, playerParticle, drawPlayerAction, psolveAction = goat.playerSetup(goat.playerWidth, 2.5, 200, 200)
# print(player, playerParticle, drawPlayerAction)
goal, drawGoalAction = goat.createGoal((1000,500,60,30), "level20", playerParticle, gloop, dplay, timer)

wall1, drawWallAction1 = goat.createWall((0,0,goat.WIDTH,100), psolveAction, goat.playerWidth)
wall2, drawWallAction2 = goat.createWall((0,100,100,goat.HEIGHT-200), psolveAction, goat.playerWidth)
wall3, drawWallAction3 = goat.createWall((goat.WIDTH-100,100,100,goat.HEIGHT-200), psolveAction, goat.playerWidth)
wall4, drawWallAction4 = goat.createWall((0,goat.HEIGHT-100,goat.WIDTH,100), psolveAction, goat.playerWidth)
wall5, drawWallAction5 = goat.createWall((400,0,50,400), psolveAction, goat.playerWidth)
wall6, drawWallAction6 = goat.createWall((800,goat.HEIGHT-400,50,400), psolveAction, goat.playerWidth)

enemy, drawEnemyAction = goat.spawnEnemy([150,430], [2,0], [150,430], [750,430], playerParticle, goat.playerWidth, "level19", gloop, dplay)
enemy2, drawEnemyAction2 = goat.spawnEnemy([250,480], [2,0], [150,480], [750,480], playerParticle, goat.playerWidth, "level19", gloop, dplay)
enemy3, drawEnemyAction3 = goat.spawnEnemy([350,530], [2,0], [150,530], [750,530], playerParticle, goat.playerWidth, "level19", gloop, dplay)
enemy4, drawEnemyAction4 = goat.spawnEnemy([450,580], [2,0], [150,580], [750,580], playerParticle, goat.playerWidth, "level19", gloop, dplay)

enemy5, drawEnemyAction5 = goat.spawnEnemy([450,130], [2,0], [450,130], [goat.WIDTH-150,130], playerParticle, goat.playerWidth, "level19", gloop, dplay)
enemy6, drawEnemyAction6 = goat.spawnEnemy([550,180], [2,0], [450,180], [goat.WIDTH-150,180], playerParticle, goat.playerWidth, "level19", gloop, dplay)
enemy7, drawEnemyAction7 = goat.spawnEnemy([650,230], [2,0], [450,230], [goat.WIDTH-150,230], playerParticle, goat.playerWidth, "level19", gloop, dplay)
enemy8, drawEnemyAction8 = goat.spawnEnemy([750,280], [2,0], [450,280], [goat.WIDTH-150,280], playerParticle, goat.playerWidth, "level19", gloop, dplay)

counter = util.make_counter()
countAction = util.make_counter_increment_action()
counter.insert_action(countAction)

coin1, drawCoinAction1 = goat.createCoin([750, 580], playerParticle, goat.playerWidth, countAction)
coin2, drawCoinAction2 = goat.createCoin([500, 130], playerParticle, goat.playerWidth, countAction)
coin3, drawCoinAction3 = goat.createCoin([1100, 130], playerParticle, goat.playerWidth, countAction)

coinwall, drawCoinWallAction = goat.createWall((850,450,400,40), psolveAction, goat.playerWidth, 3, counter)
entities.append(counter)
entities.append(coinwall)
displayActions.append(drawCoinWallAction)

entity_list = [wall1, wall2, wall3, wall4, wall5, wall6, enemy, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, coin1, coin2, coin3]
display_list = [drawWallAction1, drawWallAction2, drawWallAction3, drawWallAction4, drawWallAction5, drawWallAction6, 
				drawEnemyAction, drawEnemyAction2, drawEnemyAction3, drawEnemyAction4, drawEnemyAction5,
				drawEnemyAction6, drawEnemyAction7, drawEnemyAction8, drawCoinAction1, drawCoinAction1, drawCoinAction2, drawCoinAction3, ]

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
