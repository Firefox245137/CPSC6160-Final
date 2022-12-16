import goat
import cowmoo.engine.utility as util
import cowmoo.engine.ui as ui

hud1 = ui.make_hud( goat.WIDTH/2,100 ,"Credit:", (255, 255, 255), (0, 0, 0), size = 60)
drawHudAction1 = ui.make_hud_action()
hud1.insert_action(drawHudAction1)	

hud2 = ui.make_hud( goat.WIDTH/2,200 ,"Game Programmer / Designer", (246, 190, 0), (0, 0, 0), size = 50)
drawHudAction2 = ui.make_hud_action()
hud2.insert_action(drawHudAction2)

hud3 = ui.make_hud( goat.WIDTH/2,280 ,"Alan Wiser", (255, 255, 255), (0, 0, 0), size = 40)
drawHudAction3 = ui.make_hud_action()
hud3.insert_action(drawHudAction3)

hud4 = ui.make_hud( goat.WIDTH/2,330 ,"Joanna Lin", (255, 255, 255), (0, 0, 0), size = 40)
drawHudAction4 = ui.make_hud_action()
hud4.insert_action(drawHudAction4)

hud5 = ui.make_hud( goat.WIDTH/2,430 ,"Music / Sound", (246, 190, 0), (0, 0, 0), size = 50)
drawHudAction5 = ui.make_hud_action()
hud5.insert_action(drawHudAction5)

hud6 = ui.make_hud( goat.WIDTH/2,510 ,"\"Desert of Lost Souls\" Kevin MacLeod (incompetech.com)", (255, 255, 255), (0, 0, 0), size = 40)
drawHudAction6 = ui.make_hud_action()
hud6.insert_action(drawHudAction6)

hud7 = ui.make_hud( goat.WIDTH/2,560 ,"Licensed under Creative Commons: By Attribution 4.0 License", (255, 255, 255), (0, 0, 0), size = 30)
drawHudAction7 = ui.make_hud_action()
hud7.insert_action(drawHudAction7)

hud8 = ui.make_hud( goat.WIDTH/2,610 ,"http://creativecommons.org/licenses/by/4.0/", (255, 255, 255), (0, 0, 0), size = 30)
drawHudAction8 = ui.make_hud_action()
hud8.insert_action(drawHudAction8)

entities.append(hud1)
entities.append(hud2)
entities.append(hud3)
entities.append(hud4)
entities.append(hud5)
entities.append(hud6)
entities.append(hud7)
entities.append(hud8)
displayActions.append(drawHudAction1)
displayActions.append(drawHudAction2)
displayActions.append(drawHudAction3)
displayActions.append(drawHudAction4)
displayActions.append(drawHudAction5)
displayActions.append(drawHudAction6)
displayActions.append(drawHudAction7)
displayActions.append(drawHudAction8)
