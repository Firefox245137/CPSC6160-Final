import goat
import cowmoo.engine.utility as util

timer = util.make_timer()
startTimerAction = util.make_start_timer_action()
updateTimerAction = util.make_update_timer_action()
timer.insert_action(startTimerAction)
timer.insert_action(updateTimerAction)
player, playerParticle, drawPlayerAction, psolveAction = goat.playerSetup(goat.playerWidth, 2.5)
# print(player, playerParticle, drawPlayerAction)
goal, drawGoalAction = goat.createGoal((500,500,60,30), "level3", playerParticle, gloop, dplay)
wall, drawWallAction = goat.createWall((400,400,100,100), psolveAction, goat.playerWidth)
entities.append(player)
entities.append(playerParticle)
entities.append(goal)
entities.append(timer)
entities.append(wall)
displayActions.append(drawPlayerAction)
displayActions.append(drawGoalAction)
displayActions.append(drawWallAction)



