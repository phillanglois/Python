from random import random as rd
def points(n):
    point=[]
    for i in range(n):
        x,y=rd(),rd()
        point.append((x,y))
    return point


def ordre(A,B):
    return (A[0]<=B[0]) or (A[1]==B[1]) and (A[1]<=B[1])

def vecteur(A, B):
    return (B[0] - A[0], B[1] - A[1])
def determinant(u, v):
    return u[0] * v[1] - u[1] * v[0]

def Angle(A, B, C):
    u = vecteur(A, B)
    v = vecteur(A, C)
    return determinant(u, v)
def distance(A, B):
    x, y = vecteur(A, B)
    return x ** 2 + y ** 2
def point_min(s):
    m = s[0]
    for x in s:
        if ordre(x, m): m = x
    return m    
def comparaison(A, B, C):
    t = Angle(A, B, C)
    if t > 0: return True
    elif t < 0: return False
    else: return distance(A, B) <= distance(A, C)