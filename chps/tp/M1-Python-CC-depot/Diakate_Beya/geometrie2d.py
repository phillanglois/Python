def orientation(P:tuple,Q:tuple,R:tuple)->int:
    x=(Q[0]-P[0])
    y=(R[1]-P[1])
    z=(Q[1]-P[1])
    w=(R[0]-P[0])
    if (x*y-z*w)>0:
        return 1
    else:
        return 0

#######============================================================
import nuage
def majES(pile:list[tuple[float]], p:tuple)->list[tuple[float]]:
    nuage.trier_nuage(pile)
    while orientation(p,pile[-1],pile[-2])==0 and len(pile)!=1:
        pile.pop(-1)
    pile.append(p)
    return pile
#######============================================================

########### validation################

assert [(0, 1), (1, 1), (3, 6), (6, 8)]==majES([(0,1),(5,6),(3,6),(1,1)],(6,8))
#######===============================================
def majEL(pile:list[tuple[float]], p:tuple)->list[tuple[float]]:
    nuage.trier_nuage(pile)
    while orientation(p,pile[-1],pile[-2])==1 and len(pile)!=1:
        pile.pop(-1)
    pile.append(p)
    return pile

#######============================================================

######## validation############################
assert [(-1, 0), (0, 1), (3, 6), (5, 6), (6, 8)]==majEL([(0,1),(5,6),(3,6),(-1,0)],(6,8))



