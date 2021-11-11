#1
def creer_pile2(c):
    p = [None]*(c+1)
    p[0] = 0
    return p

def empiler2(p,x):
    p[p[0]+1]=x
    p[0] = p[0]+1
    return p    

def depiller2(p):
    p[p[0]] = None
    p[0]=p[0]-1
    return p

def taille2(p):
    return p[0]
#3
def vider_pile(p):
    for i in range(len(p)):
        p[i] = None
    p[0]=0
    return p
#4
def inverse_pile(p,p2):
    p2[0] = p[0]
    for i in range(1,p[0]+1):
        p2[i] = p[p[0]]
        p[p[0]] = p[p[0]-i]
    return p

#5
def inverse_pile22(p,p2):
    p2[0] = p[0]
    n=0
    for i in range(1,p[0]+1):
        p2[i] = p[p[0]-n]
        n=n+1
    return p2
