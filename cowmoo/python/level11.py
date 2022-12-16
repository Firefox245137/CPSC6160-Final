import goat
import cowmoo.engine.utility as util
import cowmoo.engine.ui as ui

hud = ui.make_hud( 80,50 ,"level 11", (0, 0, 0), (200, 200, 200), size = 28)
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
goal, drawGoalAction = goat.createGoal((goat.WIDTH-260,200,60,goat.HEIGHT-400), "level12", playerParticle, gloop, dplay, timer)

wall1, drawWallAction1 = goat.createWall((0,0,goat.WIDTH,200), psolveAction, goat.playerWidth)
wall2, drawWallAction2 = goat.createWall((0,200,200,goat.HEIGHT-400), psolveAction, goat.playerWidth)
wall3, drawWallAction3 = goat.createWall((goat.WIDTH-200,200,200,goat.HEIGHT-400), psolveAction, goat.playerWidth)
wall4, drawWallAction4 = goat.createWall((0,goat.HEIGHT-200,goat.WIDTH,200), psolveAction, goat.playerWidth)

counter = util.make_counter()
countAction = util.make_counter_increment_action()
counter.insert_action(countAction)

coin, drawCoinAction = goat.createCoin([600, 300], playerParticle, goat.playerWidth, countAction)
entities.append(coin)
displayActions.append(drawCoinAction)

coinwall, drawCoinWallAction = goat.createWall((700,0,50,goat.HEIGHT), psolveAction, goat.playerWidth, 1, counter)
entities.append(counter)
entities.append(coinwall)
displayActions.append(drawCoinWallAction)

enemy, drawEnemyAction = goat.spawnEnemy([770,300], [0,1], [770,200], [770,400], playerParticle, goat.playerWidth, "level11", gloop, dplay)
entities.append(enemy)
displayActions.append(drawEnemyAction)

entity_list = [wall1, wall2, wall3, wall4]
display_list = [drawWallAction1, drawWallAction2, drawWallAction3, drawWallAction4]

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



