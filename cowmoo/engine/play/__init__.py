### 
###  Entities 
### 
 
def make_frame_viewer( width, height ): 
    import cowmoo.engine.play.entity.frame_viewer as fv 
    result = fv.FrameViewer(width,height) 
    return result 

def make_game_loop(): 
    import cowmoo.engine.play.entity.game_loop as gl 
    result = gl.GameLoop() 
    return result 
 
def make_loader(game_looper, timer): 
    import cowmoo.engine.play.entity.loader as loader 
    result = loader.Loader(game_looper ,timer) 
    return result  
### 
### Actions 
### 
 
def make_terminate_action(): 
    import cowmoo.engine.play.action.terminate as tm 
    return tm.Terminate() 
 
def make_update_display_action(): 
    import cowmoo.engine.play.action.update_display as ud 
    return ud.UpdateDisplay()

def make_screen_resize_action():
    import cowmoo.engine.play.action.screen_resize as sr
    return sr.ScreenResize()
    
def make_clear_action():
    import cowmoo.engine.play.action.clear as cl
    return cl.clear()
    
def make_load_level_action():#level, mid = False):
    import cowmoo.engine.play.action.load_new_level as ll
    return ll.loadNewLevel()#level, mid = False)
