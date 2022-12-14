### 
###  Entities 
### 
 
def make_timer(): 
    import cowmoo.engine.utility.entity.timer as ti 
    result = ti.Timer()
    return result 

 
 
### 
### Actions 
### 
 
def make_activate_entity_action(): 
    import cowmoo.engine.utility.action.activate_entity as ae 
    return ae.ActivateEntity() 
 
def make_deactivate_entity_action(): 
    import cowmoo.engine.utility.action.deactivate_entity as de 
    return de.DeactivateEntity() 

def make_alarm_action(allotted): 
    import cowmoo.engine.utility.action.alarm as al 
    return al.Alarm(allotted) 

def make_start_timer_action(): 
    import cowmoo.engine.utility.action.start_timer as st 
    return st.StartTimer() 

def make_update_timer_action(): 
    import cowmoo.engine.utility.action.update_timer as ut 
    return ut.UpdateTimer() 