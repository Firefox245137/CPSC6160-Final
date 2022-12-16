import goat
import cowmoo.engine.utility as util
import cowmoo.engine.ui as ui

hud = ui.make_hud( 80,50 ,"level 12", (0, 0, 0), (200, 200, 200), size = 28)
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
goal, drawGoalAction = goat.createGoal((goat.WIDTH-260,200,60,goat.HEIGHT-400), "level13", playerParticle, gloop, dplay, timer)

wall1, drawWallAction1 = goat.createWall((0,0,goat.WIDTH,200), psolveAction, goat.playerWidth)
wall2, drawWallAction2 = goat.createWall((0,200,200,goat.HEIGHT-400), psolveAction, goat.playerWidth)
wall3, drawWallAction3 = goat.createWall((goat.WIDTH-200,200,200,goat.HEIGHT-400), psolveAction, goat.playerWidth)
wall4, drawWallAction4 = goat.createWall((0,goat.HEIGHT-200,goat.WIDTH,200), psolveAction, goat.playerWidth)

enemy, drawEnemyAction = goat.spawnEnemy([500,300], [0,1], [500,200], [500,500], playerParticle, goat.playerWidth, "level12", gloop, dplay)
enemy2, drawEnemyAction2 = goat.spawnEnemy([580,400], [0,1], [580,200], [580,500], playerParticle, goat.playerWidth, "level12", gloop, dplay)
enemy3, drawEnemyAction3 = goat.spawnEnemy([660,500], [0,1], [660,200], [660,500], playerParticle, goat.playerWidth, "level12", gloop, dplay)
enemy4, drawEnemyAction4 = goat.spawnEnemy([740,300], [0,1], [740,200], [740,500], playerParticle, goat.playerWidth, "level12", gloop, dplay)
enemy5, drawEnemyAction5 = goat.spawnEnemy([820,400], [0,1], [820,200], [820,500], playerParticle, goat.playerWidth, "level12", gloop, dplay)
enemy6, drawEnemyAction6 = goat.spawnEnemy([900,400], [0,1], [900,200], [900,500], playerParticle, goat.playerWidth, "level12", gloop, dplay)

counter = util.make_counter()
countAction = util.make_counter_increment_action()
counter.insert_action(countAction)

coin, drawCoinAction = goat.createCoin([600, 300], playerParticle, goat.playerWidth, countAction)
entities.append(coin)
displayActions.append(drawCoinAction)

coinwall, drawCoinWallAction = goat.createWall((900,0,50,goat.HEIGHT), psolveAction, goat.playerWidth, 1, counter)
entities.append(counter)
entities.append(coinwall)
displayActions.append(drawCoinWallAction)


entity_list = [wall1, wall2, wall3, wall4, enemy, enemy2, enemy3, enemy4, enemy5, enemy6, coin]
display_list = [drawWallAction1, drawWallAction2, drawWallAction3, drawWallAction4,
				drawEnemyAction, drawEnemyAction2, drawEnemyAction3, drawEnemyAction4, drawEnemyAction5, drawEnemyAction6, drawCoinAction]

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



