def make_emit_sound_action(filename, loops=0): 
    import cowmoo.engine.sound.action.emit_sound as es 
    return es.EmitSound(filename, loops) 