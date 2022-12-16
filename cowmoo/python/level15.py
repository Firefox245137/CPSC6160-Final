import goat
import cowmoo.engine.utility as util
import cowmoo.engine.ui as ui

hud = ui.make_hud( 80,50 ,"level 15", (0, 0, 0), (200, 200, 200), size = 28)
drawHudAction = ui.make_hud_action()
hud.insert_action(drawHudAction)	

timer = util.make_timer()
startTimerAction = util.make_start_timer_action()
updateTimerAction = util.make_update_timer_action()
timer.insert_action(startTimerAction)
timer.insert_action(updateTimerAction)
player, playerParticle, drawPlayerAction, psolveAction = goat.playerSetup(goat.playerWidth, 2.5, 200, 200)
goal, drawGoalAction = goat.createGoal((200,500,60,60), "level16", playerParticle, gloop, dplay, timer)

wall1, drawWallAction1 = goat.createWall((0,0,goat.WIDTH,100), psolveAction, goat.playerWidth)
wall2, drawWallAction2 = goat.createWall((0,100,100,goat.HEIGHT-200), psolveAction, goat.playerWidth)
wall3, drawWallAction3 = goat.createWall((goat.WIDTH-100,100,100,goat.HEIGHT-200), psolveAction, goat.playerWidth)
wall4, drawWallAction4 = goat.createWall((0,goat.HEIGHT-100,goat.WIDTH,100), psolveAction, goat.playerWidth)
wall5, drawWallAction5 = goat.createWall((0,goat.HEIGHT/2-50,goat.WIDTH/3*2,100), psolveAction, goat.playerWidth)
wall6, drawWallAction6 = goat.createWall((500,100,50,100), psolveAction, goat.playerWidth)
wall7, drawWallAction7 = goat.createWall((900,goat.HEIGHT-200,50,100), psolveAction, goat.playerWidth)

enemy, drawEnemyAction = goat.spawnEnemy([450,100], [0,1], [450,100], [450,goat.HEIGHT/2-80], playerParticle, goat.playerWidth, "level15", gloop, dplay)
enemy2, drawEnemyAction2 = goat.spawnEnemy([580,200], [0,1], [580,100], [580,goat.HEIGHT/2-80], playerParticle, goat.playerWidth, "level15", gloop, dplay)
enemy3, drawEnemyAction3 = goat.spawnEnemy([goat.WIDTH-180,400], [1,1], [goat.WIDTH-480,100], [goat.WIDTH-180,400], playerParticle, goat.playerWidth, "level15", gloop, dplay)
enemy4, drawEnemyAction4 = goat.spawnEnemy([1000,500], [0,1], [1000,goat.HEIGHT/2], [1000,goat.HEIGHT-130], playerParticle, goat.playerWidth, "level15", gloop, dplay)
enemy5, drawEnemyAction5 = goat.spawnEnemy([500,500], [0,1], [500,goat.HEIGHT/2+50], [500,goat.HEIGHT-130], playerParticle, goat.playerWidth, "level15", gloop, dplay)
enemy6, drawEnemyAction6 = goat.spawnEnemy([400,450], [1,0], [400,450], [800,450], playerParticle, goat.playerWidth, "level15", gloop, dplay)
enemy7, drawEnemyAction7 = goat.spawnEnemy([380,200], [0,1], [380,100], [380,goat.HEIGHT/2-80], playerParticle, goat.playerWidth, "level15", gloop, dplay)

counter = util.make_counter()
countAction = util.make_counter_increment_action()
counter.insert_action(countAction)

coin1, drawCoinAction1 = goat.createCoin([450, 150], playerParticle, goat.playerWidth, countAction)
coin2, drawCoinAction2 = goat.createCoin([580, 150], playerParticle, goat.playerWidth, countAction)
coin3, drawCoinAction3 = goat.createCoin([1100, 150], playerParticle, goat.playerWidth, countAction)
coin4, drawCoinAction4 = goat.createCoin([1100, goat.HEIGHT-200], playerParticle, goat.playerWidth, countAction)

coinwall, drawCoinWallAction = goat.createWall((300,goat.HEIGHT/2+50,40,220), psolveAction, goat.playerWidth, 4, counter)
entities.append(counter)
entities.append(coinwall)
displayActions.append(drawCoinWallAction)

entity_list = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, enemy, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, coin1, coin2, coin3, coin4]
display_list = [drawWallAction1, drawWallAction2, drawWallAction3, drawWallAction4, drawWallAction5, drawWallAction6, drawWallAction7, 
				drawEnemyAction, drawEnemyAction2,drawEnemyAction3, drawEnemyAction4, drawEnemyAction5, drawEnemyAction6, drawEnemyAction7,
				drawCoinAction1, drawCoinAction2, drawCoinAction3, drawCoinAction4]

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
