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



