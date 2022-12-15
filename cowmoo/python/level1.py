import goat

player, playerParticle, drawPlayerAction, psolveAction = goat.playerSetup(20, .5)
# print(player, playerParticle, drawPlayerAction)
goal, drawGoalAction = goat.createGoal((goat.WIDTH-60,0,60,goat.HEIGHT), "level2", playerParticle, gloop, dplay)
entities.append(player)
entities.append(playerParticle)
entities.append(goal)
displayActions.append(drawPlayerAction)
displayActions.append(drawGoalAction)



