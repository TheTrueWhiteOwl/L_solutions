# TAD stack

# Construtores
def new():
    ...

def push(x, s):
    ...

def clone(s):
    ...

# Seletores
def pop(s):
    ...

def top(s) -> int:
    ...

# Testes
def is_empty(s):
    ...

# a) (ignorar is_substack(s1, s2))
def show(s):
    pilha = clone(s)
    while not is_empty(pilha):
        print(top(pilha))
        pilha = pop(pilha)

def total(s) -> int:
    pilha = clone(s)
    soma = 0
    while not is_empty(pilha):
        soma += top(pilha)
        pilha = pop(pilha)
    
    return soma

def inverse(s):
    pilha = clone(s)
    inv = new()
    while not is_empty(pilha):
        inv = push(top(pilha), inv)
        pilha = pop(pilha)
    
    return inv

def noc(x, s) -> int:
    pilha = clone(s)
    occ = 0
    while not is_empty(pilha):
        if top(pilha) == x:
            occ += 1
        pilha = pop(pilha)
    
    return occ

def overlap(s1, s2):
    pilha = inverse(clone(s1))
    pilha_res = clone(s2)
    while not is_empty(pilha):
        pilha_res = push(top(pilha), pilha_res)
        pilha = pop(pilha)
    
    return pilha_res

# c) (ignorar is_substack(s1, s2))

from stack import *

s1 = push(1, push(2, push(3, new())))

show(s1)
"""
1
2
3
"""

print(total(s1))
# 6

s2 = inverse(s1)
show(s2)
"""
3
2
1
"""

print(noc(3,s1))
# 1

show(s1)
"""
1
2
3
"""

s4 = push(8, push(9, new()))
s5 = overlap(s4,s1)
show(s5)
"""
8
9
1
2
3
"""

from stack2 import *

s1 = push(1, push(2, push(3, new())))

show(s1)
"""
1
2
3
"""

print(total(s1))
# 6

s2 = inverse(s1)
show(s2)
"""
3
2
1
"""

print(noc(3,s1))
# 1

show(s1)
"""
1
2
3
"""

s4 = push(8, push(9, new()))
s5 = overlap(s4,s1)
show(s5)
"""
8
9
1
2
3
"""