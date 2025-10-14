def new():
    return []
    
def push(x, s):
    if isinstance(x, int) and x >= 0 and isinstance(s, list):
        return s+[x]
    else:
        raise ValueError('Argumento inválido (push).')
        
def pop(s):
    if isinstance(s, list) and len(s)>0:
        return s[:-1]
    else:
        raise ValueError('Argumento inválido (pop).')

def top(s):
    if isinstance(s, list) and len(s) > 0:
        return s[-1]  
    else:
        raise ValueError('Argumento inválido (top).')
        
def is_empty(s):
    if isinstance(s, list):
        return s == [] 
    else:
        raise ValueError('Argumento inválido (is_empty).')
        
def clone(s):
    if isinstance(s, list):
        return s[:]
    else:
        raise ValueError('Argumento inválido (is_empty).')