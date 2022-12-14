### 
###  Entities 
### 
 
def make_rectangle(bounds, color): 
    import cowmoo.engine.actor.entity.rectangle as re 
    result = re.Rectangle(bounds, color) 
    return result 

def make_circle(radius, center, color): 
    import cowmoo.engine.actor.entity.circle as ci 
    result = ci.Circle(radius, center, color) 
    return result


 
### 
### Actions 
### 
 
def make_draw_rect_action(): 
    import cowmoo.engine.actor.action.draw_rect as dr 
    return dr.DrawRect()
 
def make_draw_round_action(): 
    import cowmoo.engine.actor.action.draw_round as dc 
    return dc.DrawRound()

def make_is_inside_action(offset=0): 
    import cowmoo.engine.actor.action.is_inside as ii 
    return ii.IsInside(offset)

def make_put_position_action(): 
    import cowmoo.engine.actor.action.put_position as pp 
    return pp.PutPosition()