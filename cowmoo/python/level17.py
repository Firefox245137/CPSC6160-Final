import goat
import cowmoo.engine.utility as util
import cowmoo.engine.ui as ui

hud = ui.make_hud( 80,50 ,"level 17", (0, 0, 0), (200, 200, 200), size = 28)
drawHudAction = ui.make_hud_action()
hud.insert_action(drawHudAction)	

timer = util.make_timer()
startTimerAction = util.make_start_timer_action()
updateTimerAction = util.make_update_timer_action()
timer.insert_action(startTimerAction)
timer.insert_action(updateTimerAction)
player, playerParticle, drawPlayerAction, psolveAction = goat.playerSetup(goat.playerWidth, 2.5, 200, 200)
# print(player, playerParticle, drawPlayerAction)
goal, drawGoalAction = goat.createGoal((1000,550,60,30), "level18", playerParticle, gloop, dplay, timer)

wall1, drawWallAction1 = goat.createWall((0,0,goat.WIDTH,100), psolveAction, goat.playerWidth)
wall2, drawWallAction2 = goat.createWall((0,100,100,goat.HEIGHT-200), psolveAction, goat.playerWidth)
wall3, drawWallAction3 = goat.createWall((goat.WIDTH-100,100,100,goat.HEIGHT-200), psolveAction, goat.playerWidth)
wall4, drawWallAction4 = goat.createWall((0,goat.HEIGHT-100,goat.WIDTH,100), psolveAction, goat.playerWidth)
wall5, drawWallAction5 = goat.createWall((400,0,50,500), psolveAction, goat.playerWidth)
wall6, drawWallAction6 = goat.createWall((800,goat.HEIGHT-500,50,500), psolveAction, goat.playerWidth)
wall7, drawWallAction7 = goat.createWall((450,200,200,50), psolveAction, goat.playerWidth)
wall8, drawWallAction8 = goat.createWall((600,400,200,50), psolveAction, goat.playerWidth)

enemy, drawEnemyAction = goat.spawnEnemy([100,550], [1,0], [100,550], [770,550], playerParticle, goat.playerWidth, "level17", gloop, dplay)
enemy2, drawEnemyAction2 = goat.spawnEnemy([100,300], [1,0], [100,300], [370,300], playerParticle, goat.playerWidth, "level17", gloop, dplay)
enemy3, drawEnemyAction3 = goat.spawnEnemy([500,250], [0,1], [500,250], [500,goat.HEIGHT-130], playerParticle, goat.playerWidth, "level17", gloop, dplay)
enemy4, drawEnemyAction4 = goat.spawnEnemy([700,150], [0,1], [700,100], [700,370], playerParticle, goat.playerWidth, "level17", gloop, dplay)
enemy5, drawEnemyAction5 = goat.spawnEnemy([900,400], [1,0], [850,400], [goat.WIDTH-130,400], playerParticle, goat.playerWidth, "level17", gloop, dplay)
enemy6, drawEnemyAction6 = goat.spawnEnemy([goat.WIDTH-150,300], [1,1], [goat.WIDTH-350,100], [goat.WIDTH-150,300], playerParticle, goat.playerWidth, "level17", gloop, dplay)
enemy7, drawEnemyAction7 = goat.spawnEnemy([100,300], [1,1], [100,250], [300,450], playerParticle, goat.playerWidth, "level17", gloop, dplay)

counter = util.make_counter()
countAction = util.make_counter_increment_action()
counter.insert_action(countAction)

coin1, drawCoinAction1 = goat.createCoin([150, 500], playerParticle, goat.playerWidth, countAction)
coin2, drawCoinAction2 = goat.createCoin([700, 550], playerParticle, goat.playerWidth, countAction)
coin3, drawCoinAction3 = goat.createCoin([520, 150], playerParticle, goat.playerWidth, countAction)
coin4, drawCoinAction4 = goat.createCoin([1100, 200], playerParticle, goat.playerWidth, countAction)

coinwall, drawCoinWallAction = goat.createWall((850,450,400,40), psolveAction, goat.playerWidth, 4, counter)
entities.append(counter)
entities.append(coinwall)
displayActions.append(drawCoinWallAction)

entity_list = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, enemy, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, coin1, coin2, coin3, coin4]
display_list = [drawWallAction1, drawWallAction2, drawWallAction3, drawWallAction4, drawWallAction5,
				drawWallAction6, drawWallAction7, drawWallAction8, drawEnemyAction, drawEnemyAction2,
				drawEnemyAction3, drawEnemyAction4, drawEnemyAction5, drawEnemyAction6, drawEnemyAction7,
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



