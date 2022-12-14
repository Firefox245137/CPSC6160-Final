### 
###  Entities 
### 
 
def make_particles(): 
    import cowmoo.engine.physics.entity.particles as pa 
    result = pa.Particles()
    return result 

def make_spring_force(): 
    import cowmoo.engine.physics.entity.spring_force as sf 
    result = sf.SpringForce()
    return result 

def make_gravity_force(): 
    import cowmoo.engine.physics.entity.gravity_force as gf 
    result = gf.GravityForce()
    return result 

def make_drag_force(): 
    import cowmoo.engine.physics.entity.drag_force as df 
    result = df.DragForce()
    return result 

def make_rectangle_collider(llc, urc): 
    import cowmoo.engine.physics.entity.rectangle_collider as rc 
    result = rc.RectangleCollider(llc, urc)
    return result 

 
### 
### Actions 
### 
 
def make_euler_solve_action(): 
    import cowmoo.engine.physics.action.euler_solve as es 
    return es.EulerSolve() 

def make_position_solve_action(): 
    import cowmoo.engine.physics.action.position_solve as ps 
    return ps.PositionSolve() 

def make_velocity_solve_action(): 
    import cowmoo.engine.physics.action.velocity_solve as vs 
    return vs.VelocitySolve() 

def make_gravity_force_action(): 
    import cowmoo.engine.physics.action.gravity_force_action as gfa 
    return gfa.GravityForceAction() 

def make_spring_force_action(): 
    import cowmoo.engine.physics.action.spring_force_action as sfa 
    return sfa.SpringForceAction() 

def make_drag_force_action(): 
    import cowmoo.engine.physics.action.drag_force_action as dfa 
    return dfa.DragForceAction() 

def make_pick_position_action(index): 
    import cowmoo.engine.physics.action.pick_position as pp 
    return pp.PickPosition(index) 

def make_inside_rectangle_collider_action(): 
    import cowmoo.engine.physics.action.inside_rectangle_collider as irc 
    return irc.InsideRectangleCollider() 

def make_outside_rectangle_collider_action(): 
    import cowmoo.engine.physics.action.outside_rectangle_collider as orc 
    return orc.OutsideRectangleCollider() 

def make_activate_physics_action(forces): 
    import cowmoo.engine.physics.action.activate_physics as ap 
    return ap.ActivatePhysics(forces) 

def make_deactivate_physics_action(forces): 
    import cowmoo.engine.physics.action.deactivate_physics as dp 
    return dp.DeactivatePhysics(forces) 