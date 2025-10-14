# pyright: reportRedeclaration=false
# ^^^^^^^ this ignores redeclaration warnings for the whole script

# TAD racional

# Construtores
def cria_rac(n, d):
    ...

# Seletores
def num(r) -> int:
    ...

def den(r) -> int:
    ...

# Reconhecedores
def eh_racional(arg) -> bool:
    ...

def eh_rac_zero(arg) -> bool:
    ...

# Testes
def rac_iguais(r1,r2) -> bool:
    ...

# a)
def produto_rac(r1, r2):
    return cria_rac(num(r1)*num(r2), den(r1)*den(r2))

# b)
# {'n': <numerador>, 'd': <denominador>}

# c)
# Construtores
def cria_rac(n, d):
    rac = {
        'n': n,
        'd': d
    }
    return rac

# Seletores
def num(r) -> int:
    return r['n']

def den(r) -> int:
    return r['n']

# Reconhecedores
def eh_racional(arg) -> bool:
    return type(arg) == dict and len(arg) == 2 and ('n', 'r') in arg and \
           type(arg['n']) == type(arg['d']) == int and arg['d'] > 0

def eh_rac_zero(arg) -> bool:
    return eh_racional(arg) and arg['n'] == 0

# Testes
def rac_iguais(r1,r2) -> bool:
    return num(r1) * den(r2) == num(r2) * den(r1)

# d)
def escreve_rac(r):
    return f"{num(r)}/{den(r)}"

# e)
# (<numerador>, <denominador>)

# Construtores
def cria_rac(n, d):
    return (n, d)

# Seletores
def num(r) -> int:
    return r[0]

def den(r) -> int:
    return r[1]

# Reconhecedores
def eh_racional(arg) -> bool:
    return type(arg) == tuple and len(arg) == 2 and \
           type(arg[0]) == type(arg[1]) == int and arg[1] > 0

def eh_rac_zero(arg) -> bool:
    return eh_racional(arg) and arg[0] == 0

# Testes
def rac_iguais(r1,r2) -> bool:
    return num(r1) * den(r2) == num(r2) * den(r1)
