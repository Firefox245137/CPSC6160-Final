import goat
import cowmoo.engine.utility as util

timer = util.make_timer()
startTimerAction = util.make_start_timer_action()
updateTimerAction = util.make_update_timer_action()
timer.insert_action(startTimerAction)
timer.insert_action(updateTimerAction)
# print(timer, type(timer), updateTimerAction.__class__.__name__ == "UpdateTimer")
player, playerParticle, drawPlayerAction, psolveAction = goat.playerSetup(goat.playerWidth, 2.5, 500, 360)
# print(player, playerParticle, drawPlayerAction)
goal, drawGoalAction = goat.createGoal((goat.WIDTH-260,200,60,goat.HEIGHT-400), "level2", playerParticle, gloop, dplay)

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

wall5, drawWallAction5 = goat.createWall((700,0,50,goat.HEIGHT), psolveAction, goat.playerWidth, 1, counter)
entities.append(counter)
entities.append(wall5)
displayActions.append(drawWallAction5)

enemy, drawEnemyAction = goat.spawnEnemy([770,300], [0,1], [770,200], [770,400], playerParticle, goat.playerWidth, "level1", gloop, dplay)
entities.append(enemy)
displayActions.append(drawEnemyAction)

entities.append(player)
entities.append(playerParticle)
entities.append(goal)
entities.append(timer)
entities.append(wall1)
entities.append(wall2)
entities.append(wall3)
entities.append(wall4)
displayActions.append(drawWallAction1)
displayActions.append(drawWallAction2)
displayActions.append(drawWallAction3)
displayActions.append(drawWallAction4)
displayActions.append(drawPlayerAction)
displayActions.append(drawGoalAction)



