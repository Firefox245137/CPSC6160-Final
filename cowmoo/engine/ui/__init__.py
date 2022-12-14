### 
###  Entities 
### 
 
def make_button(bounds, color, name): 
    import cowmoo.engine.ui.entity.button as bu 
    result = bu.Button(bounds, color, name)
    return result 
 
 
### 
### Actions 
### 
 
def make_draw_button_action(): 
    import cowmoo.engine.ui.action.draw_button as db 
    return db.DrawButton() 
 

def make_press_button_action(): 
    import cowmoo.engine.ui.action.press_button as pb 
    return pb.PressButton() 