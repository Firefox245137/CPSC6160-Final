import goat
import cowmoo.engine.utility as util
import cowmoo.engine.ui as ui

hud = ui.make_hud( 80,50 ,"level 14", (0, 0, 0), (200, 200, 200), size = 28)
drawHudAction = ui.make_hud_action()
hud.insert_action(drawHudAction)	

timer = util.make_timer()
startTimerAction = util.make_start_timer_action()
updateTimerAction = util.make_update_timer_action()
timer.insert_action(startTimerAction)
timer.insert_action(updateTimerAction)
player, playerParticle, drawPlayerAction, psolveAction = goat.playerSetup(goat.playerWidth, 2.5, 200, 200)
# print(player, playerParticle, drawPlayerAction)
goal, drawGoalAction = goat.createGoal((1000,500,60,30), "level15", playerParticle, gloop, dplay, timer)

wall1, drawWallAction1 = goat.createWall((0,0,goat.WIDTH,100), psolveAction, goat.playerWidth)
wall2, drawWallAction2 = goat.createWall((0,100,100,goat.HEIGHT-200), psolveAction, goat.playerWidth)
wall3, drawWallAction3 = goat.createWall((goat.WIDTH-100,100,100,goat.HEIGHT-200), psolveAction, goat.playerWidth)
wall4, drawWallAction4 = goat.createWall((0,goat.HEIGHT-100,goat.WIDTH,100), psolveAction, goat.playerWidth)
wall5, drawWallAction5 = goat.createWall((400,0,50,400), psolveAction, goat.playerWidth)
wall6, drawWallAction6 = goat.createWall((800,goat.HEIGHT-400,50,400), psolveAction, goat.playerWidth)

enemy, drawEnemyAction = goat.spawnEnemy([600,250], [1,0], [500,250], [700,250], playerParticle, goat.playerWidth, "level14", gloop, dplay)
enemy2, drawEnemyAction2 = goat.spawnEnemy([600,250], [0,1], [600,150], [600,350], playerParticle, goat.playerWidth, "level14", gloop, dplay)
enemy3, drawEnemyAction3 = goat.spawnEnemy([600,250], [0,0], [600,150], [600,350], playerParticle, goat.playerWidth, "level14", gloop, dplay)
enemy4, drawEnemyAction4 = goat.spawnEnemy([600,250], [1,1], [500,150], [700,350], playerParticle, goat.playerWidth, "level14", gloop, dplay)

enemy5, drawEnemyAction5 = goat.spawnEnemy([900,250], [1,0], [800,250], [1100,250], playerParticle, goat.playerWidth, "level14", gloop, dplay)
enemy6, drawEnemyAction6 = goat.spawnEnemy([900,250], [0,1], [900,150], [900,450], playerParticle, goat.playerWidth, "level14", gloop, dplay)
enemy7, drawEnemyAction7 = goat.spawnEnemy([900,250], [0,0], [900,150], [900,350], playerParticle, goat.playerWidth, "level14", gloop, dplay)
enemy8, drawEnemyAction8 = goat.spawnEnemy([900,250], [1,1], [800,150], [1100,450], playerParticle, goat.playerWidth, "level14", gloop, dplay)

enemy9, drawEnemyAction9 = goat.spawnEnemy([650,500], [1,0], [550,500], [750,500], playerParticle, goat.playerWidth, "level14", gloop, dplay)
enemy10, drawEnemyAction10 = goat.spawnEnemy([650,500], [0,1], [650,400], [650,600], playerParticle, goat.playerWidth, "level14", gloop, dplay)
enemy11, drawEnemyAction11 = goat.spawnEnemy([650,500], [0,0], [650,400], [650,600], playerParticle, goat.playerWidth, "level14", gloop, dplay)
enemy12, drawEnemyAction12 = goat.spawnEnemy([650,500], [1,1], [550,400], [750,600], playerParticle, goat.playerWidth, "level14", gloop, dplay)

enemy13, drawEnemyAction13 = goat.spawnEnemy([150,400], [1,0], [150,400], [300,400], playerParticle, goat.playerWidth, "level14", gloop, dplay)
enemy14, drawEnemyAction14 = goat.spawnEnemy([200,500], [1,0], [150,500], [300,500], playerParticle, goat.playerWidth, "level14", gloop, dplay)

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

entity_list = [wall1, wall2, wall3, wall4, wall5, wall6, enemy, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8,
				enemy9, enemy10, enemy11, enemy12, enemy13, enemy14, coin1, coin2, coin3]
display_list = [drawWallAction1, drawWallAction2, drawWallAction3, drawWallAction4, drawWallAction5, drawWallAction6, 
				drawEnemyAction, drawEnemyAction2, drawEnemyAction3, drawEnemyAction4, drawEnemyAction5,
				drawEnemyAction6, drawEnemyAction7, drawEnemyAction8, drawEnemyAction9, drawEnemyAction10, drawEnemyAction11, drawEnemyAction12,
				drawEnemyAction13, drawEnemyAction14, drawCoinAction1, drawCoinAction1, drawCoinAction2, drawCoinAction3, ]

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
