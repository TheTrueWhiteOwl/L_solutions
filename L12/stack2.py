from math import *

def new():
    return 1
    
def push(x,s):
    if isinstance(x,int) and x>=0 and isinstance(s,int) and s>0:
        return s+2**(floor(log(s,2))+x+1)
    else:
        print('Argumento inválido (push).')
        
def pop(s):
    if isinstance(s,int) and s>0:
        return s-2**(floor(log(s,2)))
    else:
        print('Argumento inválido (pop).')

def top(s):
    if isinstance(s,int) and s>0:
        return floor(log(s,2))-floor(log(pop(s),2))-1
    else:
        print('Argumento inválido (top).')

def clone(s):
    return s
        
def is_empty(s):
    if isinstance(s,int) and s>0:
        return s==1
    else:
        print('Argumento inválido (is_tempty).')