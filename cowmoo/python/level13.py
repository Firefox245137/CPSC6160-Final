import goat
import cowmoo.engine.utility as util
import cowmoo.engine.ui as ui

hud = ui.make_hud( 80,50 ,"level 13", (0, 0, 0), (200, 200, 200), size = 28)
drawHudAction = ui.make_hud_action()
hud.insert_action(drawHudAction)	

timer = util.make_timer()
startTimerAction = util.make_start_timer_action()
updateTimerAction = util.make_update_timer_action()
timer.insert_action(startTimerAction)
timer.insert_action(updateTimerAction)
# print(timer, type(timer), updateTimerAction.__class__.__name__ == "UpdateTimer")
player, playerParticle, drawPlayerAction, psolveAction = goat.playerSetup(goat.playerWidth, 2.5, 300, 360)
# print(player, playerParticle, drawPlayerAction)
goal, drawGoalAction = goat.createGoal((goat.WIDTH-260,200,60,goat.HEIGHT-400), "level14", playerParticle, gloop, dplay, timer)

wall1, drawWallAction1 = goat.createWall((0,0,goat.WIDTH,200), psolveAction, goat.playerWidth)
wall2, drawWallAction2 = goat.createWall((0,200,200,goat.HEIGHT-400), psolveAction, goat.playerWidth)
wall3, drawWallAction3 = goat.createWall((goat.WIDTH-200,200,200,goat.HEIGHT-400), psolveAction, goat.playerWidth)
wall4, drawWallAction4 = goat.createWall((0,goat.HEIGHT-200,goat.WIDTH,200), psolveAction, goat.playerWidth)

enemy, drawEnemyAction = goat.spawnEnemy([350,200], [0,1], [350,200], [350,500], playerParticle, goat.playerWidth, "level13", gloop, dplay)
enemy2, drawEnemyAction2 = goat.spawnEnemy([430,500], [0,1], [430,200], [430,500], playerParticle, goat.playerWidth, "level13", gloop, dplay)
enemy3, drawEnemyAction3 = goat.spawnEnemy([510,200], [0,1], [510,200], [510,500], playerParticle, goat.playerWidth, "level13", gloop, dplay)
enemy4, drawEnemyAction4 = goat.spawnEnemy([590,500], [0,1], [590,200], [590,500], playerParticle, goat.playerWidth, "level13", gloop, dplay)
enemy5, drawEnemyAction5 = goat.spawnEnemy([670,200], [0,1], [670,200], [670,500], playerParticle, goat.playerWidth, "level13", gloop, dplay)
enemy6, drawEnemyAction6 = goat.spawnEnemy([750,500], [0,1], [750,200], [750,500], playerParticle, goat.playerWidth, "level13", gloop, dplay)
enemy7, drawEnemyAction7 = goat.spawnEnemy([830,200], [0,1], [830,200], [830,500], playerParticle, goat.playerWidth, "level13", gloop, dplay)
enemy8, drawEnemyAction8 = goat.spawnEnemy([910,500], [0,1], [910,200], [910,500], playerParticle, goat.playerWidth, "level13", gloop, dplay)
counter = util.make_counter()
countAction = util.make_counter_increment_action()
counter.insert_action(countAction)

coin, drawCoinAction = goat.createCoin([430, 450], playerParticle, goat.playerWidth, countAction)
coin2, drawCoinAction2 = goat.createCoin([590, 250], playerParticle, goat.playerWidth, countAction)
coin3, drawCoinAction3 = goat.createCoin([750, 450], playerParticle, goat.playerWidth, countAction)
coin4, drawCoinAction4 = goat.createCoin([910, 250], playerParticle, goat.playerWidth, countAction)

coinwall, drawCoinWallAction = goat.createWall((1000,0,50,goat.HEIGHT), psolveAction, goat.playerWidth, 4, counter)
entities.append(counter)
entities.append(coinwall)
displayActions.append(drawCoinWallAction)


entity_list = [wall1, wall2, wall3, wall4, enemy, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, coin, coin2, coin3, coin4]
display_list = [drawWallAction1, drawWallAction2, drawWallAction3, drawWallAction4,
				drawEnemyAction, drawEnemyAction2, drawEnemyAction3, drawEnemyAction4, drawEnemyAction5, drawEnemyAction6,
				drawEnemyAction7, drawEnemyAction8, drawCoinAction, drawCoinAction2, drawCoinAction3, drawCoinAction4]

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



