import goat
import cowmoo.engine.utility as util

timer = util.make_timer()
startTimerAction = util.make_start_timer_action()
updateTimerAction = util.make_update_timer_action()
timer.insert_action(startTimerAction)
timer.insert_action(updateTimerAction)
player, playerParticle, drawPlayerAction, psolveAction = goat.playerSetup(goat.playerWidth, 2.5)
# print(player, playerParticle, drawPlayerAction)
goal, drawGoalAction = goat.createGoal((1000,500,60,30), "level3", playerParticle, gloop, dplay)

wall1, drawWallAction1 = goat.createWall((0,0,goat.WIDTH,100), psolveAction, goat.playerWidth)
wall2, drawWallAction2 = goat.createWall((0,100,100,goat.HEIGHT-200), psolveAction, goat.playerWidth)
wall3, drawWallAction3 = goat.createWall((goat.WIDTH-100,100,100,goat.HEIGHT-200), psolveAction, goat.playerWidth)
wall4, drawWallAction4 = goat.createWall((0,goat.HEIGHT-100,goat.WIDTH,100), psolveAction, goat.playerWidth)
wall5, drawWallAction5 = goat.createWall((400,0,50,400), psolveAction, goat.playerWidth)
wall6, drawWallAction6 = goat.createWall((800,goat.HEIGHT-400,50,400), psolveAction, goat.playerWidth)


entities.append(player)
entities.append(playerParticle)
entities.append(goal)
entities.append(timer)
entities.append(wall1)
entities.append(wall2)
entities.append(wall3)
entities.append(wall4)
entities.append(wall5)
entities.append(wall6)
displayActions.append(drawWallAction1)
displayActions.append(drawWallAction2)
displayActions.append(drawWallAction3)
displayActions.append(drawWallAction4)
displayActions.append(drawWallAction5)
displayActions.append(drawWallAction6)
displayActions.append(drawPlayerAction)
displayActions.append(drawGoalAction)




