import goat

player, playerParticle, drawPlayerAction, psolveAction = goat.playerSetup(20, .5)
# print(player, playerParticle, drawPlayerAction)
goal, drawGoalAction = goat.createGoal((500,500,60,30), "level3", playerParticle, gloop, dplay)
wall, drawWallAction = goat.createWall((400,400,100,100), psolveAction, goat.playerWidth)
entities.append(player)
entities.append(playerParticle)
entities.append(goal)
entities.append(wall)
displayActions.append(drawPlayerAction)
displayActions.append(drawGoalAction)
displayActions.append(drawWallAction)



