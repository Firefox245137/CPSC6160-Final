import goat
import cowmoo.engine.utility as util

timer = util.make_timer()
startTimerAction = util.make_start_timer_action()
updateTimerAction = util.make_update_timer_action()
timer.insert_action(startTimerAction)
timer.insert_action(updateTimerAction)
player, playerParticle, drawPlayerAction, psolveAction = goat.playerSetup(goat.playerWidth, 2.5)
goal, drawGoalAction = goat.createGoal((500,500,60,30), "level2", playerParticle, gloop, dplay)
wall, drawWallAction = goat.createWall((400,400,100,100), psolveAction, goat.playerWidth)
enemy, drawEnemyAction = goat.spawnEnemy([250,250], [1,0], [150,250], [350,250], playerParticle, goat.playerWidth)
entities.append(player)
entities.append(playerParticle)
entities.append(goal)
entities.append(wall)
entities.append(timer)
entities.append(enemy)
displayActions.append(drawPlayerAction)
displayActions.append(drawGoalAction)
displayActions.append(drawWallAction)
displayActions.append(drawEnemyAction)



