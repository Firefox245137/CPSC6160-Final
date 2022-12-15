import goat

player, playerParticle, drawPlayerAction = goat.playerSetup(20, .5)
# print(player, playerParticle, drawPlayerAction)
goal, drawGoalAction = goat.createGoal((500,500,60,30), "level2", playerParticle, gloop, dplay)
entities.append(player)
entities.append(playerParticle)
entities.append(goal)
displayActions.append(drawPlayerAction)
displayActions.append(drawGoalAction)



